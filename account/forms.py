# -*- coding: utf-8 -*-
import re
import datetime

from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import PasswordResetForm as OldPaswordResetForm
from django.contrib.auth.forms import UserChangeForm as OldUserChangeForm
from django.contrib.sites.models import get_current_site
from django.template import RequestContext, loader
from django.utils.http import int_to_base36
from django.contrib.localflavor.us.forms import USZipCodeField
from django.forms.widgets import Widget, Select, CheckboxInput
from django.utils.dates import MONTHS
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from tiger.forms import PCISafeCharField

from account.models import UserProfile
from common.forms import AjaxModelForm
from common.models import ABR_STATE_CHOICES as STATE_CHOICES
from famdates.account.models import Interest
from django.utils.encoding import force_unicode
from django.utils.html import conditional_escape
from itertools import chain
from django.forms import extras
from famdates.common.models import ABR_STATE_CHOICES
from famdates.events.models import Event
from famdates.notification.models import Notification

RE_DATE = re.compile(r'(\d{4})-(\d\d?)-(\d\d?)$')


class MonthYearWidget(Widget):
    """
    A Widget that splits date input into two <select> boxes for month and year,
    with 'day' defaulting to the first of the month.

    Based on SelectDateWidget, in 

    django/trunk/django/forms/extras/widgets.py


    """
    none_value = (0, '---')
    month_field = '%s_month'
    year_field = '%s_year'

    def __init__(self, attrs=None, years=None, required=True):
        # years is an optional list/tuple of years to use in the "year" select box.
        self.attrs = attrs or {}
        self.required = required
        if years:
            self.years = years
        else:
            this_year = datetime.date.today().year
            self.years = range(this_year, this_year + 10)

    def render(self, name, value, attrs=None):
        try:
            year_val, month_val = value.year, value.month
        except AttributeError:
            year_val = month_val = None
            if isinstance(value, basestring):
                match = RE_DATE.match(value)
                if match:
                    year_val, month_val, day_val = [int(v) for v in match.groups()]

        output = []

        if 'id' in self.attrs:
            id_ = self.attrs['id']
        else:
            id_ = 'id_%s' % name

        month_choices = MONTHS.items()
        if not (self.required and value):
            month_choices.append(self.none_value)
        month_choices.sort()
        local_attrs = self.build_attrs(id=self.month_field % id_)
        s = Select(choices=month_choices)
        select_html = s.render(self.month_field % name, month_val, local_attrs)
        output.append(select_html)

        year_choices = [(i, i) for i in self.years]
        if not (self.required and value):
            year_choices.insert(0, self.none_value)
        local_attrs['id'] = self.year_field % id_
        s = Select(choices=year_choices)
        select_html = s.render(self.year_field % name, year_val, local_attrs)
        output.append(select_html)

        return mark_safe(u'\n'.join(output))

    def id_for_label(self, id_):
        return '%s_month' % id_

    id_for_label = classmethod(id_for_label)

    def value_from_datadict(self, data, files, name):
        y = data.get(self.year_field % name)
        m = data.get(self.month_field % name)
        if y == m == "0":
            return None
        if y and m:
            return '%s-%s-%s' % (y, m, 1)
        return data.get(name, None)


class UserChangeForm(OldUserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget.attrs = {'class': 'hidden'}
        self.fields['password'].help_text = '<a href=\"password/\">Click here to reset password.</a>'
        self.fields['groups'].help_text = ''
        self.fields['username'].help_text = ''
        username = [f for f in self.instance._meta.fields if f.name == 'username'][0]
        username.state_filter = True


class UpdateUserForm(forms.ModelForm):
    email_error_message = u'This email address is already in use.'
    password_error_message = u'The two password fields do not match.'

    email = forms.EmailField(label='Email', max_length=75)
    password = forms.CharField(
        label=u'Password',
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'}),
        min_length=6
    )
    confirm_password = forms.CharField(
        label=u'Password confirmation',
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'}),
        min_length=6
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')


class CreateUserForm(forms.ModelForm):
    email_error_message = u'This email address is already in use.'
    password_error_message = u'The two password fields do not match.'

    email = forms.EmailField(label='Email', max_length=75)
    password = forms.CharField(
        label=u'Password',
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'}),
        min_length=6,
    )
    confirm_password = forms.CharField(
        label=u'Password confirmation',
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'}),
        min_length=6,
        required=False,
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email', u'')
        email = email.lower()

        if email and User.objects.filter(email=email).exists():
            if self.instance.email != email:
                raise forms.ValidationError(u'This email address is already in use.')
        return email

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password', u'')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(self.password_error_message)
        return confirm_password


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    next_redirect = forms.CharField(widget=forms.HiddenInput, required=False)


class RegistrationFromStep1(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField(required=False)
    email = forms.EmailField()
    email = forms.EmailField()


class PasswordResetForm(OldPaswordResetForm):
    def save(self, domain_override=None, email_template_name='account/reset_email.html', subject_template_name=None,
             use_https=False, token_generator=default_token_generator, from_email=None, request=None):

        from django.core.mail import EmailMultiAlternatives

        for user in self.users_cache:
            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override

            c = {
                'email': user.email,
                'domain': domain,
                'site_name': site_name,
                'uid': int_to_base36(user.id),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': use_https and 'https' or 'http',
            }

            Notification.send(recipients=[user.email, ], template='password_reset', ctx=c)


GENDER = (('male', "Male"),
          ('female', "Female"))

ACCOUNT_TYPE = (('individual', "Individual"),
                ('business', "Team, Business or Organization"))

EMAIL_NOTIFICATIONS = (('enabled', "Enable Email Notification"),
                       ('disabled', "Disable Email notification"))


class EmailNotification(AjaxModelForm):
    email_notification = forms.ChoiceField(widget=forms.RadioSelect, choices=EMAIL_NOTIFICATIONS, initial='enabled',
                                           required=False)
    blocked_users = forms.ModelMultipleChoiceField(User.objects.all(),
                                                   widget=forms.SelectMultiple(
                                                       attrs={'data-placeholder': 'Type to find users',
                                                              'width': '400px'}),
                                                   required=False)

    class Meta:
        model = UserProfile
        fields = ('email_notification', 'receive_email_from_groups', 'receive_email_for_new_message', 'blocked_users')


class CreateProfileForm(AjaxModelForm):
    tags = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Comma separated list'}))

    acct_type = forms.ChoiceField(label="Account Type", widget=forms.RadioSelect, choices=ACCOUNT_TYPE)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER, required=False)
    email = forms.EmailField(required=True)
    confirm_email = forms.EmailField(required=True)
    state = forms.CharField(required=False,
                            widget=forms.Select(attrs={'placeholder': 'State'}, choices=ABR_STATE_CHOICES))
    first_name = forms.CharField()
    hide_birthday = forms.BooleanField(initial=False, required=False)
    show_month_day = forms.BooleanField(initial=False, required=False)
    birthday = forms.DateField(required=False,
                               widget=extras.SelectDateWidget(years=range(1900, datetime.date.today().year)))
    date_founded = forms.DateField(required=False,
                                   widget=extras.SelectDateWidget(years=range(1900, datetime.date.today().year)))
    avatar = forms.FileField(required=False, widget=forms.FileInput)
    background = forms.FileField(label="Profile Banner", required=False, widget=forms.FileInput)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput)

    zipcode = forms.CharField(required=True)

    class Meta:
        model = UserProfile
        exclude = ('user', 'interests', 'default_interest_feed', 'email_notification')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password', u'')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Confirm password does not match")
        return confirm_password

    def clean_gender(self):
        if self.data.get('acct_type') == 'individual':
            if not self.cleaned_data.get('gender', u''):
                raise forms.ValidationError("Gender is required for individual")

        return self.cleaned_data.get('gender', u'')

    def clean_date_founded(self):
        if self.data.get('acct_type') == 'business':
            if not self.cleaned_data.get('date_founded', u''):
                raise forms.ValidationError("Date Founded is required for business or team")

        return self.cleaned_data.get('date_founded', u'')

    def clean_confirm_email(self):
        email = self.cleaned_data.get('email', u'')

        confirm_email = self.cleaned_data.get('confirm_email')

        if confirm_email and email != confirm_email:
            raise forms.ValidationError("Confirm email does not match")
        return confirm_email

        return email

    def clean(self):
        if self.data.get('acct_type') == 'individual':
            birthday = self.cleaned_data.get('birthday', u'')
            if not birthday:
                self._errors["birthday"] = "Birthday is required"
            else:
                years = (datetime.datetime.now().date() - birthday).days / 365.25
                if years < 13:
                    self._errors["birthday"] = "You must be 13 or older"

        return self.cleaned_data


class UpdateProfileForm(CreateProfileForm):
    email = forms.EmailField(required=True)
    confirm_email = forms.EmailField(required=False)
    password = forms.CharField(required=False, widget=forms.PasswordInput)
    confirm_password = forms.CharField(required=False, widget=forms.PasswordInput)


    def clean(self):
        cleaned_data = super(UpdateProfileForm, self).clean()
        email = self.cleaned_data.get('email', u'')
        confirm_email = self.cleaned_data.get('confirm_email', u'')

        if self.instance and self.instance.pk and email != User.objects.get(pk=self.instance.user.pk).email:
            if not confirm_email:
                self._errors["confirm_email"] = "Confirm email is required"

        return cleaned_data


PROFILE_TYPE = (('free_business', 'Free Account'),
                ('premium_business', 'Business Premium Account'))

CREDIT_CARD_TYPE = (
    ('visa', 'Visa'),
    ('master card', 'Master Card'),
)


class CreateBusinessProfileAjaxForm(AjaxModelForm):
    profile_type = forms.ChoiceField(widget=forms.RadioSelect, choices=PROFILE_TYPE)
    # payment fields
    card_type = forms.ChoiceField(choices=CREDIT_CARD_TYPE, label=_('Card Type'), required=False)
    card_number = PCISafeCharField(label=_('Card Number'), required=False)
    expiration_date = forms.CharField(widget=MonthYearWidget(), label=_('Expiration Date'), required=False)
    verification_number = PCISafeCharField(max_length=4, label=_('Verification Number'),
                                           help_text="Last 3 digits on the back of your card. For AmEx, 4 digits on the first",
                                           required=False)
    card_name = forms.CharField(max_length=200, label=_('Name on Card'), required=False)
    billing_address = forms.CharField(max_length=200, label=_('Address'), required=False)
    billing_address_2 = forms.CharField(max_length=200, required=False, label=_('Address (line 2)'))
    city = forms.CharField(max_length=50, label=_('City'), required=False)
    state = forms.ChoiceField(choices=STATE_CHOICES, label=_('State'), required=False)
    zip = USZipCodeField(label=_('Zip'), required=False)
    stripe_token = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = UserProfile
        fields = ('phone', 'profile_type',)


class CreateUserAjaxForm(AjaxModelForm, CreateUserForm):
    pass


class GroupTabCheckboxSelectMultiple(forms.SelectMultiple):
    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = []
        has_id = attrs and 'id' in attrs
        final_attrs = self.build_attrs(attrs, name=name)

        tab_id = 1
        active = 'active'
        output = [u'<div class="tab-content">', ]
        initial_qs = self.choices.queryset

        nav = ['<ul class="nav nav-tabs">', ]

        for tab in 'general, NHL, CFL, MLS, MLB, WNBA, NBA, NFL, UEFA-English, college-div1'.split(', '):
            nav.append('<li class="%s">' % active)
            nav.append('<a href="#%s-tab%d" data-toggle="tab">%s</a>' % (
            name, tab_id, tab.replace('college-div1', 'College Div1')))
            nav.append('</li>')

            output = output + [u'<div class="tab-pane %s" id="%s-tab%d">' % (active, name, tab_id), u'<ul>']
            tab_id += 1
            if tab_id != 1:
                active = ''

            # Normalize to strings
            str_values = set([force_unicode(v) for v in value])
            self.choices.queryset = initial_qs.filter(sub_category=tab)
            for i, (option_value, option_label) in enumerate(chain(self.choices, choices)):
                # If an ID attribute was given, add a numeric index as a suffix,
                # so that the checkboxes don't all have the same ID attribute.
                if has_id:
                    final_attrs = dict(final_attrs, id='%s_%s_%s' % (attrs['id'], i, tab.lower()))
                    label_for = u' for="%s"' % final_attrs['id']
                else:
                    label_for = ''

                cb = CheckboxInput(final_attrs, check_test=lambda value: value in str_values)
                option_value = force_unicode(option_value)
                rendered_cb = cb.render(name, option_value)
                option_label = conditional_escape(force_unicode(option_label))
                output.append(u'<li><label%s>%s %s</label></li>' % (label_for, rendered_cb, option_label))
            output.append(u'</ul>')
            output.append(u'</div>')

        nav.append('</ul>')

        output.append(u'</div>')

        output = nav + output

        return mark_safe(u'\n'.join(output))

    def id_for_label(self, id_):
        # See the comment for RadioSelect.id_for_label()
        if id_:
            id_ += '_0'
        return id_


class UserInterestForm(AjaxModelForm):
    fan_zone_interests = forms.ModelMultipleChoiceField(widget=GroupTabCheckboxSelectMultiple(),
                                                        queryset=Interest.objects.filter(
                                                            category__name='fan_zone').order_by('name'))
    fitness_nutrition_interests = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(),
                                                                 queryset=Interest.objects.filter(
                                                                     category__name='fitness_nutrition').order_by(
                                                                     'name'))
    game_time_interests = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(),
                                                         queryset=Interest.objects.filter(
                                                             category__name='game_time').order_by('name'))

    #     default_interest_feed = forms.ModelChoiceField(widget=forms.RadioSelect(), queryset=InterestCategory.objects.exclude(name='my teams'), required=True, initial=1)

    class Meta:
        model = UserProfile
        fields = ('fan_zone_interests', 'fitness_nutrition_interests', 'game_time_interests' )

class CreateEventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = (
            'name',
            'details',
            'type',
            'beginning',
            'time',
            'duration',
            'interval',
            'frequency',
            'repetitions',
            'end'
        )



class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birthday', 'acct_type', 'hide_birthday', 'gender', 'profile_type', 'date_founded', 'show_month_day' )

    birthday = forms.DateField(required=False,
                               widget=extras.SelectDateWidget(years=range(1900, datetime.date.today().year)))

    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

class Signup3Form(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('address', 'attn', 'city', 'zipcode', 'state', )


from ajax_upload.widgets import AjaxClearableFileInput

class Signup4Form(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('about_me', 'use_gravatar', 'avatar', 'background')

        widgets = {
            'avatar': AjaxClearableFileInput,
            'background': AjaxClearableFileInput,
        }
