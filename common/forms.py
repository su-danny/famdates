from django import forms
from django.conf import settings
from django.template.defaultfilters import striptags

# add support for twitter bootstrap
try:
    from bootstrap.forms import BootstrapModelForm as SUIStyleModelForm, BootstrapForm as SUIStyleForm
except:
    from django.forms import ModelForm as SUIStyleModelForm, Form as SUIStyleForm


class AjaxBaseForm(forms.BaseForm):
    def errors_as_json(self, strip_tags=False):
        error_summary = {}
        errors = {}
        for error in self.errors.iteritems():
            if self.prefix:
                errors.update({self.prefix + '-' + error[0]: unicode(striptags(error[1]) \
                    if strip_tags else error[1])})
            else:
                errors.update({error[0]: unicode(striptags(error[1]) \
                    if strip_tags else error[1])})
        error_summary.update({'errors': errors})
        return error_summary


class AjaxModelForm(AjaxBaseForm, SUIStyleModelForm):
    """Ajax Form class for ModelForms"""


class AjaxForm(AjaxBaseForm, SUIStyleForm):
    """Ajax Form class for Forms"""
    
    
    