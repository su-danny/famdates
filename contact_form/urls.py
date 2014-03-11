from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
                       url(r'^$',
                           'contact_form.views.contact', name='main-contact'),
                       url(r'^sent$',
                           direct_to_template,
                           {'template': 'contact_form/message_sent.html'},
                           name="message_sent"),
)
