from django.conf.urls import patterns, include, url
from django.conf import settings

from account.views import RegistrationView, ProfileView, PasswordSetView, BusinessRegistrationView, BusinessFirstLoginView
from account.forms import PasswordResetForm

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import contact_form
from famdates.post.views import CreatePost
from django.contrib.auth.decorators import login_required

admin.autodiscover()

from post.models import Post
from voting.views import vote_on_object

urlpatterns = patterns('',
                       url(r'^ajax-upload/', include('ajax_upload.urls')),
                       url(r'^$', 'sf.views.home', name='home'),
                       url(r'^message/', include('messages.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^follow/', include('follow.urls')),
                       url(r'^contact-us/', include('contact_form.urls')),
                       url(r'^account/login/$', 'account.views.login_page', name='login_page'),
                       url(r'^account/logout/$', 'account.views.logout_user', name='logout_user'),
                       url(r'^registration/$', RegistrationView.as_view(), name='registration'),
                       url(r'^registration/business$', BusinessRegistrationView.as_view(),
                           name='business_registration'),
                       url(r'^account/profile/$', ProfileView.as_view(), name='account_profile'),
                       url(r'^account/family_profile/$', ProfileView.as_view(), name='account_family_profile'),
                       url(r'^account/edit_profile/$', 'account.views.edit_profile', name='edit_profile'),
                       url(r'^account/business/first_time/$', BusinessFirstLoginView.as_view(),
                           name='business_first_time'),
                       url(r'^account/profile/(?P<id>(\d+))$', 'account.views.public_profile_detail',
                           {
                               'template_name': 'account/public_profile_detail.html',
                           },
                           name='public_profile_detail'
                       ),
                       url(r'^registration/update_interests$', 'account.views.update_interests',
                           {
                               'template_name': 'account/update_interests.html',
                               'extra_context': {'next': '/registration/recommend_similar_users'}
                           },
                           name='update_interests'
                       ),
                       url(r'^registration/recommend_similar_users$', 'account.views.recommend_similar_user',
                           {
                               'template_name': 'account/recommend_similar_users.html',
                               'extra_context': {'next': '/'}
                           },
                           name='recommend_similar_user'
                       ),
                       url(r'^account/similar_users$', 'account.views.recommend_similar_user',
                           {
                               'template_name': 'account/recommend_similar_users.html',
                               'extra_context': {'next': '/'}
                           },
                           name='account_similar_users'
                       ),
                       url(r'^account/password/$', 'django.contrib.auth.views.password_change',
                           {
                               'template_name': 'account/change_password.html',
                               'extra_context': {'next': '/'}
                           },
                           name='password_change'
                       ),
                       url(r'^account/password/done/$',
                           'django.contrib.auth.views.password_change_done',
                           {
                               'template_name': 'account/change_password.html',
                               'extra_context': {'success': True, 'next': '/'}
                           },
                           name='password_change_done'
                       ),
                       url(r'^account/password/set/$', PasswordSetView.as_view(), name='password_set'),

                       url(r'^account/reset/$', 'django.contrib.auth.views.password_reset',
                           {
                               'template_name': 'account/reset_form.html',
                               'email_template_name': 'account/reset_email.html',
                               'password_reset_form': PasswordResetForm,
                               'from_email': 'no-reply@famdates.com',
                               'extra_context': {'next': '/'}
                           },
                           name='password_reset'
                       ),
                       url(r'^account/reset/done/$', 'django.contrib.auth.views.password_reset_done',
                           {
                               'template_name': 'account/reset_form.html',
                               'extra_context': {'success': True, 'next': '/'}
                           },
                           name='password_reset_done'
                       ),
                       url(r'^account/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
                           'django.contrib.auth.views.password_reset_confirm',
                           {
                               'template_name': 'account/reset_confirm.html',
                               'extra_context': {'next': '/'}
                           },
                           name='password_reset_confirm'
                       ),
                       url(r'^account/reset/complete/$',
                           'django.contrib.auth.views.password_reset_complete',
                           {
                               'template_name': 'account/reset_confirm.html',
                               'extra_context': {'success': True, 'next': '/'}
                           },
                           name='password_reset_complete'
                       ),
                       url(r'^search$',
                           'search.views.simple_search',
                           name='search'
                       ),
                       url(r'^search/people$',
                           'search.views.similar_user_search',
                           {
                           },
                           name='search_people'
                       ),
                       url(r'^fan-zone$',
                           login_required(CreatePost.as_view()),
                           {
                               'feed': 'fan_zone',
                               'feed_type': 'fan_zone'
                           },
                           name='fan-zone-feed'
                       ),
                       url(r'^fitness-nutrition$',
                           login_required(CreatePost.as_view()),
                           {
                               'feed': 'fitness_nutrition',
                               'feed_type': 'fitness_nutrition'
                           },
                           name='fitness-nutrition-feed'
                       ),
                       url(r'^game-time$',
                           login_required(CreatePost.as_view()),
                           {
                               'feed': 'game_time',
                               'feed_type': 'game_time'
                           },
                           name='game-time-feed'
                       ),
                       # Generic view to vote on Link objects
                       (r'^post/(?P<object_id>\d+)/(?P<direction>up|down|clear)vote/?$',
                        vote_on_object, dict(model=Post, template_object_name='post',
                                             template_name='kb/link_confirm_vote.html',
                                             allow_xmlhttprequest=True)),
                       url(r'^post/', include('post.urls')),
                       url(r'^group/', include('group.urls')),
                       url(r'^account/update_email_notification/$', 'account.views.update_email_notification',
                           name='update_email_notification'),
                       url(r'^account/deactivate/$', 'account.views.deactivate', name='account_deactivated'),
                       url(r'^news/', include('news.urls')),
                       url(r'^upload/', include('fileupload.urls')),
                       url(r'^account/(?P<profile_id>\d+)/images/view$', 'account.views.images_view',
                           dict(template_name="account/images_view.html"), name='account_images_view'),
                       url(r'^account/(?P<profile_id>\d+)/interests/view$', 'account.views.interests_view',
                           dict(template_name="account/interests_view.html"), name='account_interests_view'),
                       url(r'^account/(?P<profile_id>\d+)/followings/view$', 'account.views.followings_view',
                           dict(template_name="account/followings_view.html"), name='account_followings_view'),
                       url(r'^account/(?P<profile_id>\d+)/folllower/view$', 'account.views.followers_view',
                           dict(template_name="account/followers_view.html"), name='account_followers_view'),
                       url(r'^account/images/edit$', 'account.views.images_edit',
                           dict(template_name="account/images_edit.html"), name='account_images_edit'),
                       url(r'^account/interests/edit$', 'account.views.interests_edit',
                           dict(template_name="account/interests_edit.html"), name='account_interests_edit'),
                       url(r'^account/followings/edit$', 'account.views.followings_view',
                           dict(template_name="account/followings_view.html", profile_id=None),
                           name='account_followings_edit'),
                       url(r'^account/followers/edit$', 'account.views.followers_edit',
                           dict(template_name="account/followers_edit.html"), name='account_followers_edit'),
                       url(r'^account/images/remove/(?P<id>\d+)$', 'account.views.remove_image', name="remove_image"),
                       url(r'^account/interests/remove/(?P<id>\d+)$', 'account.views.remove_interest',
                           name="remove_interest"),
                       url(r'^account/interests/add/(?P<id>\d+)$', 'account.views.add_interest',
                           name="add_interest"),

                       url(r'^account/followers/remove/(?P<id>\d+)$', 'account.views.remove_follower',
                           name="remove_follower"),
                       url(r'^account/fb/friends', 'account.views.get_fb_friends', name="account_get_fb_friends"),
                       url(r'^account/invite/do_friends', 'account.views.do_invite_friends',
                           name="account_do_invite_friends"),
                       url(r'^account/invite/friends', 'account.views.invite_friends', name="account_invite_friends"),
                       url(r'^account/home$', 'account.views.account_home', name="account_home"),
                       url(r'^account/event$', 'account.views.account_event', name="account_event"),
                       url(r'^account/event/create', 'account.views.create_event', name="create_event"),
                       url(r'^account/signup/(?P<step>\d+)$', 'account.views.signup', name="account_signup"),
                       url(r'^account/join-event/(?P<event_id>\d+)$', 'account.views.join_event', name="join_event"),
                       url(r'^chat/', include('chat.urls')),
                       url(r'^event/live$', 'events.views.live_events', name="live_events"),
                       url(r'^event/detail/(?P<event_id>\d+)$', 'events.views.details', name="event_details"),
                       url(r'^notification$', 'notification.views.user_notifications', name="user_notifications"),
                       url(r'', include('social_auth.urls')),
                       url(r"", include("django_socketio.urls")),
)

if True or settings.SERVER == 'local':
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT}),
    )



