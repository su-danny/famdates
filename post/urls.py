from django.conf.urls.defaults import *
from django.views.generic import RedirectView, list_detail

from .views import *
from famdates.post.views import CreatePost

urlpatterns = patterns('',
                       url(r'create/$', CreatePost.as_view(), name='create_post'),
                       url(r'create/(?P<feed>[\w.@+-]+)/$', CreatePost.as_view(), name='create_post_for_feed'),
                       url(r'^comment/(?P<post_id>\d+)/create$', create_comment, name='create_comment'),
                       # url(r'^comment/delete/(?P<pk>\d+)$', delete_comment, name='delete_comment'),
                       url(r'close/(?P<pk>\d+)$', close_sticky_post, name='close_sticky_post'),
                       url(r'delete/(?P<pk>\d+)$', delete_post, name='delete_post'),
                       url(r'comments$', comments, name="comments"),
                       url(r'$', posts, name="post_list"),
)
