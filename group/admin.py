from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from .models import *

admin.site.register((Group,))