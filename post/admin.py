from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

admin.site.register((Post, ))
admin.site.register(StickyClosedPost)
