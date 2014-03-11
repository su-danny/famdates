import json
import logging

from django.views.generic.simple import direct_to_template

try:
    from urlparse import parse_qs
except ImportError:
    from cgi import parse_qs

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Count
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


def home(request, template="home.html"):
    if not request.user.is_authenticated():
        return render(request, template, {})
    else:
        try:
            profile = request.user.get_profile()
            if profile.current_registration_step:
                return render(request, template, {'current_registration_step': profile.current_registration_step})
        except:
            pass

        return redirect('/account/home')
    