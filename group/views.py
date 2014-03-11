from django.views.generic import CreateView
from .models import *
from .forms import *
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json
from famdates.common.utils import json_view
from django.db.models import Q


class CreateGroup(CreateView):
    model = Group
    form_class = GroupForm

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CreateGroup, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs['groups'] = Group.objects.filter(is_private=False)
        kwargs['my_groups'] = Group.objects.filter(usergroup__user=self.request.user)
        return kwargs

    def form_valid(self, form):
        ret = super(CreateGroup, self).form_valid(form)

        if self.request.is_ajax():
            return HttpResponse('{"success": True}', mimetype='application/json')
        else:
            return ret


@login_required
def edit(request, pk=None, template_name="group/index.html"):
    instance = my_groups = all_groups = None
    ret = {'success': True}

    if pk:
        instance = Group.objects.get(pk=pk)
        template_name = "group/edit.html"

    form = GroupAjaxForm(instance=instance)

    if request.method == 'GET':
        my_groups = Group.objects.filter(Q(owner=request.user) | Q(usergroup__user=request.user))
        all_groups = Group.objects.filter()

    if request.method == 'POST':
        form = GroupAjaxForm(request.POST, request.FILES, instance=instance)

        if not form.is_valid():
            errors = form.errors_as_json(strip_tags=True)
            profile_form_errors = form.errors_as_json(strip_tags=True)

            errors = dict(errors['errors'].items() + profile_form_errors['errors'].items())
            ret.update({'errors': errors, 'success': False})
        else:
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()

        if request.is_ajax:
            return HttpResponse(json.dumps(ret), 'application/json')

    ctx = {"form": form,
           "all_groups": all_groups,
           "my_groups": my_groups,
           "instance": instance}

    return render(request, template_name, ctx)


def detail(request, pk, template_name='group/detail.html'):
    group = get_object_or_404(Group, pk=pk)
    ctx = {'group': group, 'joined': UserGroup.objects.filter(user=request.user, group=group).count() > 0}
    return render(request, template_name, ctx)


@login_required
@json_view
def join_group(request, group_pk):
    if request.method == 'POST':
        ug = UserGroup.objects.filter(user=request.user, group__pk=group_pk)[:1]
        if ug:
            ug = ug[0]
            ug.invitation_accepted = True
            ug.save()
        else:
            UserGroup.objects.create(user=request.user, group=Group.objects.get(pk=group_pk))

        return {'sucess': True}

    return {'success': False}


@login_required
@json_view
def create_message(request, group_pk):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            msg = Message(content=content, group=Group.objects.get(pk=group_pk),
                          author=request.user, parent=request.POST.get('parent', None))
            msg.save()
        else:
            return {'success': False, 'message': 'empty message'}

        return {'success': True, 'message': {'pk': msg.pk}}

    return {'success': False}


@login_required
def accept_invitation(request, invitation_code):
    ug = get_object_or_404(UserGroup, invitation_code=invitation_code)
    ug.invitation_accepted = True
    ug.save()
    return redirect('/group/#my_groups')


@csrf_exempt
@login_required
@json_view
def invite(request, group_pk):
    success = False
    group = Group.objects.get(pk=group_pk)
    name_or_email = request.POST.get('name_or_email')
    if name_or_email and group.send_inivitation(request, name_or_email):
        success = True

    return {'success': success}    
    
    
    