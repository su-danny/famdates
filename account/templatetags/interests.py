import datetime
from django import template
from famdates.account.models import Interest

register = template.Library()


@register.simple_tag(takes_context=True)
def get_interests(context, format_string):
    context['interests'] = Interest.objects.all()
    return ''