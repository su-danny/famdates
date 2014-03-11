from django.core.exceptions import ImproperlyConfigured
from django.conf import settings
from django import template

register = template.Library()


@register.simple_tag
def stripe_pub_key():
    if hasattr(settings, 'STRIPE_PUB_KEY'):
        return settings.STRIPE_PUB_KEY
    raise ImproperlyConfigured("STRIPE_PUB_KEY is not set.")