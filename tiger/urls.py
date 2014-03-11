from django.conf.urls.defaults import patterns, include, url
from .views import manage_cards, receive_webhook, edit_card, delete_card, make_default_card

urlpatterns = patterns('',
                       url(r'^manage/$', manage_cards, name='tiger_manage_cards'),
                       url(r'^add_card/$', edit_card, name='tiger_add_card'),
                       url(r'^delete_card/(?P<card_id>\d+)/$', delete_card, name='tiger_delete_card'),
                       url(r'^make_default/(?P<card_id>\d+)/$', make_default_card, name='tiger_make_default_card'),
                       url(r'^receive_webhook/$', receive_webhook, name='tiger_receive_webhook')
)