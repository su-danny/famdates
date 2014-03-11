# -*- coding: utf-8 -*-
import json
import logging

from django.views.generic.simple import direct_to_template
from famdates.account.forms import UserInterestForm, UpdateUserForm, \
    EmailNotification, UpdateProfileForm
from famdates.account.models import UserProfile
from famdates.post.models import Post, StickyClosedPost, MediaPost
from django.contrib.auth import logout
from famdates.fileupload.models import MediaFile
from famdates.common.utils import json_view
from django.views.decorators.csrf import csrf_exempt
from famdates.follow.models import Follow
from famdates.notification.models import Notification
from StringIO import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from account.models import Interest

try:
    from urlparse import parse_qs
except ImportError:
    from cgi import parse_qs

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.db.models import Count, Q
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.admin.views.main import ChangeList as OldChangeList
from django.conf import settings
from django.views.generic import TemplateView, DetailView, FormView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.middleware.csrf import get_token
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.files import File
from tagging.models import Tag

from forms import (LoginForm, CreateProfileForm, CreateUserForm, UpdateUserForm, \
                   CreateBusinessProfileAjaxForm, CreateUserAjaxForm, CreateEventForm, Signup3Form)
from models import FacebookSession, FacebookSessionError
from famdates.events.forms import EventForm
from famdates.events.models import Event
from datetime import date, time


def login_page(request):
    context = {'pageTitle': 'Login'}
    error = None
    next_redirect = request.GET.get('next', settings.LOGIN_REDIRECT_URL)

    if request.user.is_authenticated():
        logout(request)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if 'next_redirect' in request.POST:
            next_redirect = request.POST['next_redirect']

        if form.is_valid():
            try:
                user = auth.authenticate(username=form.cleaned_data['email'],
                                         password=form.cleaned_data['password'])
            except:
                user = None

            if user is not None:
                if user.is_active:
                    user.backend = 'django.contrib.auth.backends.ModelBackend'
                    auth.login(request, user)
                    if request.is_ajax():
                        return HttpResponse(json.dumps({'success': True}))

                    if next_redirect:
                        return redirect(next_redirect)
                    return redirect('/')

        if request.is_ajax():
            return HttpResponse(json.dumps({'success': False}))

        context.update(
            {'formError': u'Either the email or password you entered is incorrect.'}
        )
    else:
        form = LoginForm(initial={'next_redirect': next_redirect})

    if request.GET:
        if 'facebook' in request.GET:
            fb_cookie_name = 'fbs_%s' % settings.FACEBOOK_APP_ID
            fb_cookie = request.COOKIES.get(fb_cookie_name, None)
            if fb_cookie:
                fb_session = parse_qs(fb_cookie, True)

                access_token = fb_session['access_token'][0]
                expires = fb_session['expires'][0]

                facebook_session = FacebookSession.objects.get_or_create(access_token=access_token)[0]
                facebook_session.expires = expires
                facebook_session.save()

                try:
                    user = auth.authenticate(token=access_token)
                except FacebookSessionError:
                    facebook_session.delete()

                    if next:
                        response = HttpResponseRedirect('.?next=' + next)
                    else:
                        response = HttpResponseRedirect('.')
                    response.delete_cookie(fb_cookie_name)
                    return response

                if user:
                    if user.is_active:
                        auth.login(request, user)
                        if next:
                            response = redirect(next)
                        else:
                            response = redirect('home')

                        response.set_cookie('user_name', str(user.get_full_name()), domain='.famdates.com')
                        if user.profile.facebook_uid:
                            response.set_cookie('user_fid', user.profile.facebook_uid, domain='.famdates.com')

                        return response

                    else:
                        error = 'AUTH_DISABLED'
                else:
                    return redirect('registration')

    context.update({'error': error, 'form': form, 'next': next or ''})
    return render(request, 'account/login.html', context)


def logout_user(request):
    auth.logout(request)
    next = request.REQUEST.get('next', None)
    if next:
        response = redirect(next)
    else:
        response = redirect('home')
    return response


@login_required
def public_profile_detail(request, id, template_name="public_profile_detail.html"):
    profile = get_object_or_404(UserProfile, id=id)
    similar_users = profile.get_similar_profiles()
    ctx = {
        'profile': profile,
        'similar_users': similar_users,
        'similar_user_count': len(similar_users),
        'posts': Post.objects.filter(author=profile.user),
        'public_events': Event.objects.all(),
    }

    if profile.is_private and not Follow.objects.is_following(request.user, profile):
        template_name = "account/private_profile_detail.html"

    return render(request, template_name, ctx)


class RegistrationView(TemplateView):
    template_name = 'account/registration.html'
    user_form_class = CreateUserAjaxForm
    profile_form_class = CreateProfileForm


    def dispatch(self, request, *args, **kwargs):
        profile = None
        if request.user.is_authenticated():
            self.user_form = self.user_form_class(instance=request.user)

            try:
                profile = request.user.get_profile()
                self.profile_form = self.profile_form_class(instance=profile)

            except UserProfile.DoesNotExist:
                pass
        else:
            self.user_form = self.user_form_class(
                initial={'email': request.GET.get('email'), 'first_name': request.GET.get('first_name')})

        if not profile:
            self.profile_form = self.profile_form_class()

        return super(RegistrationView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RegistrationView, self).get_context_data(**kwargs)
        context.update({
            'user_form': self.user_form,
            'profile_form': self.profile_form
        })
        return context

    def form_valid(self, request):
        password = self.user_form.cleaned_data['confirm_password']
        user = self.user_form.save(commit=False)
        user.username = hash(self.user_form.cleaned_data['email'])
        user.email = self.user_form.cleaned_data['email']
        user.set_password(password)
        user.save()
        profile = self.profile_form.save(commit=False)

        if not profile.pk:
            # default values for notification
            profile.receive_email_from_groups = True
            profile.receive_email_for_new_message = True

        profile.user = user
        profile.save()

        try:

            if not request.user.is_authenticated():
                auth_user = auth.authenticate(username=user.username, password=password)
                auth.login(self.request, auth_user)

                # Send out notification
                Notification.send(recipients=[user.email, ], template='account_signup', ctx={'user': user})

        except Exception, e:
            print 'Can not send out notification ', e

        return redirect("home")

    def post(self, request, *args, **kwargs):
        user = None
        profile = None

        if request.user.is_authenticated():
            user = request.user
            try:
                profile = request.user.get_profile()

                self.user_form = self.user_form_class(request.POST, instance=user)
                self.profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)

            except UserProfile.DoesNotExist:
                pass
        else:
            self.user_form = self.user_form_class(request.POST, instance=user)
            self.profile_form = self.profile_form_class(request.POST, request.FILES, instance=profile)

        if self.user_form.is_valid() and self.profile_form.is_valid():
            ret = self.form_valid(request)

            profile = self.profile_form.instance
            if request.FILES.get('background'):
                profile = UserProfile.objects.get(pk=profile.pk)
                profile.background_cropped = profile.background
                profile.save()

            if request.POST.get('x', 0):
                from PIL import Image

                try:
                    im_width = int(round(float(request.POST.get('im_width', 1200))))
                    im_height = int(round(float(request.POST.get('im_height', 200))))

                    im = Image.open(profile.background.path)
                    (o_w, o_h) = im.size
                    ratio = o_w / float(request.POST.get('background_displayed_width', o_w))

                    x = int(round(float(request.POST.get('x', 0)) * ratio))
                    y = int(round(float(request.POST.get('y', 0)) * ratio))

                    x2 = int(round(float(request.POST.get('x2', 0)) * ratio))
                    y2 = int(round(float(request.POST.get('y2', 0)) * ratio))

                    size = (im_width, im_height)

                    cropped_im = im.crop((x, y, x2, y2))
                    edit_img = cropped_im.resize(size, Image.BICUBIC)

                    tempfile_io = StringIO()
                    edit_img.save(tempfile_io, 'JPEG')

                    img = InMemoryUploadedFile(tempfile_io, None, str(profile.id) + '_background.jpg', 'image/jpeg',
                                               tempfile_io.len, None)

                    profile = UserProfile.objects.get(pk=profile.pk)
                    profile.background = img
                    profile.save()

                except Exception, e:
                    print e

            if request.is_ajax():
                return HttpResponse(json.dumps(
                    {'success': True, 'background': settings.MEDIA_URL + str(profile and profile.background)}),
                                    mimetype='application/json')
            else:
                return ret

        elif request.is_ajax():
            response = {'success': False}

            profile_form_errors = self.profile_form.errors_as_json(strip_tags=True)
            user_form_errors = self.user_form.errors_as_json(strip_tags=True)
            errors = user_form_errors['errors'].items() + profile_form_errors['errors'].items()
            response.update({'errors': errors})
            return HttpResponse(json.dumps(response), mimetype='application/json')

        return self.get(request, *args, **kwargs)


class BusinessRegistrationView(TemplateView):
    template_name = 'account/business_registration.html'
    user_form_class = CreateUserAjaxForm
    profile_form_class = CreateBusinessProfileAjaxForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('home')
            #            return redirect('profile')

        self.user_form = self.user_form_class()
        self.profile_form = self.profile_form_class()
        return super(BusinessRegistrationView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BusinessRegistrationView, self).get_context_data(**kwargs)
        context.update({
            'user_form': self.user_form,
            'profile_form': self.profile_form
        })
        return context

    def form_valid(self, request):
        password = self.user_form.cleaned_data['confirm_password']
        user = self.user_form.save(commit=False)
        user.username = self.user_form.cleaned_data['email']
        user.set_password(password)
        user.save()
        profile = self.profile_form.save(commit=False)
        profile.user = user
        profile.save()

        auth_user = auth.authenticate(username=user.username, password=password)
        auth.login(self.request, auth_user)

        if request.is_ajax():
            return HttpResponse(json.dumps({'success': True}), mimetype='application/json')

        return redirect("home")

    def post(self, request, *args, **kwargs):
        self.user_form = self.user_form_class(request.POST)
        self.profile_form = self.profile_form_class(request.POST)

        if self.user_form.is_valid() and self.profile_form.is_valid():
            return self.form_valid(request)
        elif request.is_ajax():
            response = {'success': False}
            user_form_errors = self.user_form.errors_as_json(strip_tags=True)
            profile_form_errors = self.profile_form.errors_as_json(strip_tags=True)

            errors = dict(user_form_errors['errors'].items() + profile_form_errors['errors'].items())
            response.update({'errors': errors})

            return HttpResponse(json.dumps(response), mimetype='application/json')

        return self.get(request, *args, **kwargs)


class ProfileView(TemplateView):
    template_name = 'account/activity.html'
    context_object_data = 'user'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ProfileView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        from django.contrib.sites.models import Site

        current_site = Site.objects.get_current()

        try:
            profile = self.get_object().get_profile()
        except UserProfile.DoesNotExist:
            profile = UserProfile(user=self.get_object())
            profile.save();

        similar_users = profile.get_similar_profiles()

        following_users = [profile.user for profile in profile.get_following_profiles()]

        context.update({
            'current_site': current_site,
            'pageTitle': u'My Profile',
            'profile': profile,
            'similar_users': similar_users,
            'similar_user_count': len(similar_users),
            'posts': Post.objects.filter(author=self.request.user). \
                exclude(pk__in=[sp.post.pk for sp in StickyClosedPost.objects.filter(user=self.request.user)]).order_by(
                '-created'),
            'feed': self.kwargs.get('feed', 'main feed').replace('_', ' ').upper(),
            'public_events': Event.objects.all()
        })
        return context

    def get_object(self):
        return self.request.user


class PasswordSetView(FormView):
    template_name = 'account/change_password.html'
    form_class = SetPasswordForm
    model = User

    def get_success_url(self):
        return reverse('password_change_done')

    def get_form_kwargs(self):
        kwargs = super(PasswordSetView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(PasswordSetView, self).form_valid(form)


class BusinessFirstLoginView(TemplateView):
    template_name = 'account/business_first_login.html'
    context_object_data = 'user'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(BusinessFirstLoginView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BusinessFirstLoginView, self).get_context_data(**kwargs)
        return context

    def get_object(self):
        return self.request.user


def update_interests(request, extra_context, template_name="update_interests.html"):
    if request.GET.get('step') == '5':
        request.user.get_profile().update_registration_step('5')
        qs = Interest.objects.filter(category__name='fan_zone')

        fan_zones = []
        for tab in 'general, NHL, CFL, MLS, MLB, WNBA, NBA, NFL, UEFA-English, college-div1'.split(', '):
            groups = {'': []}
            for interest in qs.filter(sub_category=tab):
                if interest.group:
                    if interest.group.name not in groups:
                        groups[interest.group.name] = [interest, ]
                    else:
                        groups[interest.group.name].append(interest)
                else:
                    groups[''].append(interest)

            three_group_pages = []
            three_items = []
            for g in groups.items():
                three_items.append(g)
                if len(three_items) > 2:
                    three_group_pages.append(three_items)
                    three_items = []

            if three_items:
                three_group_pages.append(three_items)

            fan_zones.append((tab, three_group_pages))

        ctx = {'form': UserInterestForm(),
               'fan_zones': fan_zones}
        template_name = 'account/signup-5.html'
    elif request.GET.get('step') == '6':
        request.user.get_profile().update_registration_step('6')
        ctx = {'interests': Interest.objects.filter(category__name='fitness_nutrition').order_by('name')}
        template_name = 'account/signup-6.html'
    elif request.GET.get('step') == '7':
        request.user.get_profile().update_registration_step('7')

        ctx = {'interests': Interest.objects.filter(category__name='game_time').order_by('name')}
        template_name = 'account/signup-7.html'

    if request.method == 'POST':
        form = UserInterestForm(request.POST, instance=request.user.get_profile())
        if form.is_valid():
            form.save()
            if request.is_ajax():
                return HttpResponse('{"success": true}', 'application/json')

            return redirect(extra_context.get('next', '/'))
        else:
            if request.is_ajax():
                return HttpResponse(json.dumps(form.errors_as_json(strip_tags=True)), 'application/json')

        ctx['form'] = form

    return render(request, template_name, ctx)


@login_required
def update_email_notification(request):
    if request.method == 'POST' and request.is_ajax():
        form = EmailNotification(request.POST, instance=request.user.get_profile())
        if form.is_valid():
            form.save()
            return HttpResponse('{"success": true}', 'application/json')
        else:
            return HttpResponse(json.dumps(form.errors_as_json(strip_tags=True)), 'application/json')

    return HttpResponse('{"success": false}', 'application/json')


@login_required
def deactivate(request, template_name="account/deactivated.html"):
    if request.method == 'POST':
        profile = request.user.get_profile()
        profile.deactivated = True
        profile.save()

        logout(request)

    logout(request)

    return redirect('/')


@login_required
def edit_profile(request, template_name="account/edit_profile.html"):
    profile = request.user.get_profile()

    ctx = {'form': UserInterestForm(instance=profile),
           'user_form': UpdateUserForm(instance=request.user),
           'profile_form': UpdateProfileForm(instance=profile),
           'email_notification_form': EmailNotification(instance=profile)
    }

    if request.method == 'POST':
        form = UserInterestForm(request.POST, instance=request.user.get_profile())
        if form.is_valid():
            form.save()

        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()

        profile_form = UpdateProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()

        ctx['form'] = form
        ctx['user_form'] = user_form
        ctx['profile_form'] = profile_form

    return render(request, template_name, ctx)


def recommend_similar_user(request, extra_context, template_name):
    similar_profiles = None
    if request.user.is_authenticated():
        if request.is_ajax():
            if request.GET.get('complete'):
                # Selecting similar users is the final step
                request.user.get_profile().update_registration_step('')
            else:
                template_name = 'account/signup-8.html'
                similar_profiles = request.user.get_profile().get_similar_profiles(group_by_category=True)
        else:
            similar_profiles = request.user.get_profile().get_similar_profiles()

        ctx = {'similar_profiles': similar_profiles}

    return render(request, template_name, ctx)


@login_required
def images_edit(request, template_name):
    ctx = {'media': MediaFile.objects.filter(post__author=request.user)}

    return render(request, template_name, ctx)


@login_required
def followers_edit(request, template_name):
    profile = request.user.get_profile()
    ctx = {'followers': Follow.objects.get_follows(profile)}

    return render(request, template_name, ctx)


@login_required
def interests_edit(request, template_name):
    profile = request.user.get_profile()
    ctx = {'interests': list(profile.fan_zone_interests.all()) + list(profile.game_time_interests.all()) + list(
        profile.fitness_nutrition_interests.all())}

    return render(request, template_name, ctx)


@csrf_exempt
@json_view
@login_required
def remove_image(request, id):
    ret = {'success': False}

    if request.method == "POST":
        MediaFile.objects.get(pk=id).delete()
        ret = {"success": True}

    return ret


@csrf_exempt
@json_view
@login_required
def remove_interest(request, id):
    ret = {'success': False}
    profile = request.user.get_profile()
    if request.method == "POST":
        profile.game_time_interests.remove(id)
        profile.fitness_nutrition_interests.remove(id)
        profile.fan_zone_interests.remove(id)
        ret = {"success": True}

    return ret


@csrf_exempt
@json_view
@login_required
def add_interest(request, id):
    ret = {'success': False}
    profile = request.user.get_profile()
    if request.method == "POST":
        profile.game_time_interests.add(id)
        profile.fitness_nutrition_interests.add(id)
        profile.fan_zone_interests.add(id)
        ret = {"success": True}

    return ret


@csrf_exempt
@json_view
@login_required
def remove_follower(request, id):
    ret = {'success': False}
    profile = request.user.get_profile()
    if request.method == "POST":
        from follow.utils import unfollow

        unfollow(UserProfile.objects.get(pk=id).user, profile)
        ret = {"success": True}
    return ret


@json_view
@login_required
def get_fb_friends(request):
    success = False
    results = []
    try:
        from social_auth.models import UserSocialAuth

        usa = UserSocialAuth.objects.get(user=request.user)
        token = usa.extra_data['access_token']
        from facepy import GraphAPI

        graph = GraphAPI(token)
        results = graph.get('me/friends')
        success = True
    except:
        pass

    return {'success': success, 'results': results}


@csrf_exempt
@json_view
@login_required
def do_invite_friends(request, template='account/invite_friends.html'):
    success = False
    results = []
    if request.method == 'POST':
        import json

        data = json.loads(request.POST.get('json'))

        try:
            from social_auth.models import UserSocialAuth

            usa = UserSocialAuth.objects.get(user=request.user)
            token = usa.extra_data['access_token']
            from famdates.facepy import GraphAPI

            graph = GraphAPI(token)

            for friend in data.get('fbFriends'):
                if friend.get('checked'):
                    results.append(friend.get('id'))

            success = True
        except Exception, e:
            print e

        for friend in data.get('friendEmails'):
            try:
                Notification.send(template='friend_invite',
                                  recipients=[friend['email'], ],
                                  ctx={'friend': request.user, 'user': {'first_name': friend['name']}})
            except Exception, e:
                print e
    return {'success': success, 'results': results}


@login_required
def invite_friends(request, template='account/invite_friends.html'):
    return render(request, template, {})


@login_required
def account_home(request, template='account/home.html'):
    ctx = {'feed': 'HOME'}
    interests = Interest.objects.all()
    try:
        profile = request.user.get_profile()
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
        profile.save()

    if request.is_ajax():
        template = 'modules/posts.html'

    if True:
        following_users = [profile.user for profile in profile.get_following_profiles()]

        posts = Post.objects.filter(Q(author=request.user) | Q(author__in=following_users)).exclude(
            is_sticky=True).order_by('-created')
        feeds = []

        for feed in ('fan_zone', 'fitness_nutrition', 'game_time'):
            if request.GET.get(feed, 'false') == 'true':
                feeds.append(feed)

        if feeds:
            posts = posts.filter(feed__in=feeds)

        ctx['posts'] = posts
        ctx['interests'] = interests
        ctx['upcoming_events'] = Event.objects.filter(beginning__gte=date.today()).order_by('-beginning')

    return render(request, template, ctx)


@login_required
def images_view(request, profile_id, template_name):
    profile = get_object_or_404(UserProfile, pk=profile_id)
    ctx = {
        'profile': profile,
        'media': MediaPost.objects.filter(post__author=profile.user),
        'photos': profile.get_photos()
    }

    if request.user == profile.user:
        template_name = 'account/images_edit.html'

    return render(request, template_name, ctx)


@login_required
def interests_view(request, profile_id, template_name):
    profile = get_object_or_404(UserProfile, pk=profile_id)
    ctx = {
        'profile': profile,
        'interests': profile.interests,
    }

    return render(request, template_name, ctx)


@login_required
def followers_view(request, profile_id, template_name):
    profile = get_object_or_404(UserProfile, pk=profile_id)

    ctx = {
        'profile': profile,
        'followers': profile.get_following_profiles(),
        'enable_blocking': False,
    }

    return render(request, template_name, ctx)


@login_required
def followings_view(request, template_name, profile_id=None):
    enable_blocking = False
    if profile_id:
        profile = get_object_or_404(UserProfile, pk=profile_id)
    else:
        profile = request.user.get_profile()
        enable_blocking = True

    ctx = {
        'profile': profile,
        'followings': profile.get_following_profiles(),
        'enable_blocking': enable_blocking,
    }

    return render(request, template_name, ctx)


@login_required
def account_event(request):
    user = UserProfile(user=request.user)
    print user
    event = user.events.all()
    return HttpResponse(json.dumps(
        [dict(beginning=e.beginning,
              time=e.beginning, ) for e in event]))


@csrf_exempt
@login_required
def create_event(request):
    context = {}
    ret = {'success': True}
    form = EventForm(request.POST)

    if form.is_valid():
        profile = request.user.get_profile()
        obj = form.save(commit=False)
        obj.related_object = profile
        obj.save()
    else:
        ret = {'success': False, 'errors': [str(e) for e in form.errors]}

    if not request.is_ajax():
        context.update({'form': form})
        return render(request, 'account/event.html', context)

    return HttpResponse(json.dumps(ret))


from .forms import CreateProfileForm, Signup4Form
import json


def signup3(request, ret):
    profile = request.user.get_profile()
    form = Signup3Form(request.POST, instance=profile)
    if form.is_valid():
        form.save()
        profile.current_registration_step = '4'
        profile.save()
    else:
        ret = {'success': False, 'errors': [str(e) for e in form.errors]}

    return ret


def signup4(request, ret):
    profile = request.user.get_profile()
    form = Signup4Form(request.POST, instance=profile)
    if form.is_valid():
        form.save()
        profile.current_registration_step = '5'
        profile.save()
    else:
        ret = {'success': False, 'errors': [str(e) for e in form.errors]}

    return ret


def signup(request, step):
    ret = {
        'success': True
    }

    if step == '1':
        from django.contrib.auth import login, logout

        logout(request)
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email

            user.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'

            UserProfile.objects.create(user=user, current_registration_step='2')

            login(request, user)
        else:
            ret = {'success': False, 'errors': [str(e) for e in form.errors]}

    if step == '2':
        profile = request.user.get_profile()
        form = CreateProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

            data = form.cleaned_data
            if data['acct_type'] == 'individual':
                user = request.user
                user.first_name = data.get('first_name')
                user.last_name = data.get('last_name')
                user.save()

                profile.current_registration_step = '3'
                profile.save()
        else:
            print 'form is not valid'

    if step == '3':
        ret = signup3(request, ret)

    if step == '4':
        ret = signup4(request, ret)

    return HttpResponse(json.dumps(ret))


@csrf_exempt
@json_view
@login_required
def join_event(request, event_id):
    ret = {'success': False}
    profile = request.user.get_profile()
    if request.method == "POST":
        profile.join_event(event_id)
        ret = {"success": True}
    return ret

