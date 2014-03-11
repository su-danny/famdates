from django import forms
from .models import *
from common.forms import AjaxModelForm


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = ('owner', 'created', )


class GroupAjaxForm(AjaxModelForm):
    class Meta:
        model = Group
        exclude = ('owner', 'created')
        
        