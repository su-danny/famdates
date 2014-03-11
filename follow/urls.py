from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       url(r'^toggle/(?P<app>[^\/]+)/(?P<model>[^\/]+)/(?P<id>\d+)/$', 'follow.views.toggle',
                           name='toggle'),
                       url(r'^toggle/(?P<app>[^\/]+)/(?P<model>[^\/]+)/(?P<id>\d+)/$', 'follow.views.toggle',
                           name='follow'),
                       url(r'^toggle/(?P<app>[^\/]+)/(?P<model>[^\/]+)/(?P<id>\d+)/$', 'follow.views.toggle',
                           name='unfollow'),
                       url(r'^block/(?P<app>[^\/]+)/(?P<model>[^\/]+)/(?P<id>\d+)/$', 'follow.views.block',
                           name='block_url'),
)
