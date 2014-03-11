from django.views.generic import CreateView
from settings import ITEM_PER_PAGE
from famdates.post.models import Post, Comment, StickyClosedPost, \
    MediaPost
from famdates.post.forms import PostForm
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from famdates.common.utils import json_view
import json
from famdates.fileupload.models import MediaFile
from famdates.notification.models import Notification

from django.conf import settings
from django.db.models import Q
from events.models import Event
from datetime import date


class CreatePost(CreateView):
    model = Post
    form_class = PostForm

    def get_context_data(self, **kwargs):
        feed = self.kwargs.get('feed', 'main_feed')
        kwargs[feed] = True
        m = {'fitness_nutrition': 'Fitness & Nutrition'}
        kwargs['feed'] = m.get(feed, feed).replace('_', ' ').upper()
        kwargs['feed_type'] = feed

        profile = self.request.user.get_profile()
        kwargs['posts'] = Post.objects.filter(feed=self.kwargs.get('feed')).order_by('-created')[
                          :settings.ITEM_PER_PAGE]
        profile.update_stats(feed)

        if self.request.GET.get('is_ajax'):
            self.template_name = "modules/posts.html"

        return kwargs

    def form_invalid(self, form):
        ret = {'success': False, 'errors': form.errors.values()}
        return HttpResponse(json.dumps(ret), 'application/json')

    def form_valid(self, form):
        try:
            form.instance.author = self.request.user
            wall = self.request.POST.get('wall')

            if wall:
                form.instance.wall = User.objects.get(pk=wall)

            if self.kwargs.get('feed'):
                form.instance.feed = self.kwargs.get('feed')
                form.save()

            success_url = self.request.POST.get('success_url')
            if success_url: self.success_url = self.request.path_info

            form.instance.feed = self.request.POST.get('feed', '')

            print self.request.POST.get('feed', '')

            location = self.request.POST.get('location', '')
            form.instance.location = location
            form.instance.is_sticky = self.request.POST.get('is_sticky', '') == 'on'

            uploaded_files = self.request.POST.get('uploaded_files', '')

            if uploaded_files:
                uploaded_files = json.loads(uploaded_files)
            else:
                uploaded_files = []

            post = form.save()
            if uploaded_files:
                for file in uploaded_files:
                    try:
                        # the file can be deleted before being added to this post
                        post.media.add(file)
                    except:
                        pass

            ret = {'success': True}
        except Exception, e:
            ret = {'success': False}

        return HttpResponse(json.dumps(ret), 'application/json')


@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    hash = ''

    profile = post.author.get_profile()

    if request.method == 'POST':
        comment = Comment(body=request.POST.get('body'))
        comment.author = request.user
        comment.post = post
        comment.save()
        hash = '#c' + str(comment.id)

        # Create notification
        if profile.get_settings('notification_for_new_comment'):
            Notification(recipients=post.author.email,
                                        sent_from='webmaster@famdates.com',
                                        subject='You have a new comment ' + request.META['HTTP_REFERER'] + hash,
                                        body='na',
                                        html_body='na',
                                        send_by_email=False).save()

    return redirect(request.META['HTTP_REFERER'] + hash)


@login_required
@csrf_exempt
def close_sticky_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        try:
            tracking = StickyClosedPost.objects.create(user=request.user, post=post)
            tracking.save()
            return HttpResponse('{"success": true}', content_type='application/json')
        except:
            pass

    return HttpResponse('{"success": false}', content_type='application/json')


@login_required
@csrf_exempt
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        try:
            post.delete()
            return HttpResponse('{"success": true}', content_type='application/json')
        except:
            pass

    return HttpResponse('{"success": false}', content_type='application/json')


@login_required
def posts(request, template="modules/posts.html"):
    ctx = {
        'posts': Post.objects.filter(feed__in=request.GET.get('feed').split(',')).filter(id__lt=request.GET.get('lt', '10000000')).order_by(
            '-created')[:settings.ITEM_PER_PAGE],
        'profile': request.user.get_profile(),
        'upcoming_events': Event.objects.filter(beginning__gte=date.today()).order_by('-beginning')
    }
    return render(request, template, ctx)


@login_required
def comments(request):
    profile = request.user.get_profile()
    following_users = [profile.user for profile in profile.get_following_profiles()]
    user_comments = Comment.objects.filter(Q(post__author=request.user) | Q(post__author__in=following_users)).order_by(
        '-created')

    return HttpResponse(json.dumps(
        [dict(body=c.body,
              id=c.id,
              timestamp=c.created.strftime("%b. %d %Y"),
              author=c.author.get_profile().get_full_name) for c in user_comments]))
