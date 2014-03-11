from django.conf.urls.defaults import *
from django.views.generic import RedirectView, list_detail

from .views import feed

urlpatterns = patterns('',
                       url(r'^(?P<name>[\w.@+-]+)$', feed, name='news_index'),
)
