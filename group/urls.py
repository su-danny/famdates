from django.conf.urls.defaults import *
from .views import *

urlpatterns = patterns('',
                       url(r'^$', edit, name='group_index'),
                       url(r'^(?P<pk>\d+)$', detail, name='group_detail'),
                       url(r'^(?P<pk>\d+)/edit$', edit, name='group_edit'),
                       url(r'^accept/(?P<invitation_code>\d+)$', accept_invitation, name='group_accept_invitation'),
                       url(r'^(?P<group_pk>\d+)/invite$', invite, name='group_invite'),
                       url(r'^(?P<group_pk>\d+)/message/create$', create_message, name='group_create_message'),
                       url(r'^(?P<group_pk>\d+)/join$', join_group, name='group_join'),
)
