import re
import datetime

from django.forms.widgets import Widget, Select
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.utils.dates import MONTHS
from django.contrib.localflavor.us.forms import USStateField, USZipCodeField
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.forms.util import flatatt

from common.models import ABR_STATE_CHOICES as STATE_CHOICES
from common.forms import AjaxForm


class PCISafeTextInput(forms.TextInput):
    def render(self, name, value, attrs=None):
        """
        Don't include the name in the rendered HTML, so
        value never gets POSTed to the server.
        """
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type)
        if value != None:
            final_attrs['value'] = force_unicode(self._format_value(value))
            final_attrs['autocomplete'] = 'off'
        return mark_safe('<input%s />' % flatatt(final_attrs))


class PCISafeCharField(forms.CharField):
    widget = PCISafeTextInput

    def clean(self, *args, **kwargs):
        return ""


CARD_CHOICES = {
    ('Visa', 'Visa'),
    ('American Express', 'American Express'),
    ('MasterCard', 'MasterCard'),
    ('Discover', 'Discover'),
    ('JCB', 'JCB'),
    ('Diners Club', 'Diners Club')
}

# commented for easy preference
#class CreditCardForm(forms.Form):
#    """
#    Form that renders all widgets, but only expects a 'stripe_token' in the
#    POSTed response, for easy PCI compliance.
#    
#    Note that no server side field validation is performed.
#    """
#    cc_type = forms.ChoiceField(choices=CARD_CHOICES)
#    cc_number = PCISafeCharField()
#    #expires = ExpiryDateField()
#    ccv = PCISafeCharField(max_length=4)
#    name = forms.CharField(max_length=200)
#    address_line_1 = forms.CharField(max_length=200)
#    address_line_2 = forms.CharField(max_length=200)
#    city = forms.CharField(max_length=200)
#    state = USStateField()
#    zipcode = USZipCodeField()

__all__ = ('MonthYearWidget',)

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


CREDIT_CARD_TYPE = (
    ('visa', 'Visa'),
    ('master card', 'Master Card'),
)


class CreditCardForm(AjaxForm):
    """
    Form that renders all widgets, but only expects a 'stripe_token' in the
    POSTed response, for easy PCI compliance.
    
    Note that no server side field validation is performed.
    """
    card_type = forms.ChoiceField(choices=CREDIT_CARD_TYPE, label=_('Card Type'))
    card_number = PCISafeCharField(label=_('Card Number'))
    expiration_date = forms.CharField(widget=MonthYearWidget(), label=_('Expiration Date'))
    verification_number = PCISafeCharField(max_length=4, label=_('Verification Number'),
                                           help_text="Last 3 digits on the back of your card. For AmEx, 4 digits on the first")
    card_name = forms.CharField(max_length=200, label=_('Name on Card'))
    billing_address = forms.CharField(max_length=200, label=_('Address'))
    billing_address_2 = forms.CharField(max_length=200, required=False, label=_('Address (line 2)'))
    city = forms.CharField(max_length=50, label=_('City'))
    state = forms.ChoiceField(choices=STATE_CHOICES, label=_('State'))
    zip = USZipCodeField(label=_('Zip'))
    stripe_token = forms.CharField(widget=forms.HiddenInput())