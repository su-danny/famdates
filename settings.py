# -*- coding: utf-8 -*-

import os
import sys
import socket

PROJECT_PATH = os.path.dirname(__file__)
HOSTNAME = socket.gethostname()

# Stage settings
if 'stage' in HOSTNAME:
    from settings_local import *

# Local settings
else:
    from settings_local import *

ADMINS = (
    ('Ben', 'ben@simpleunion.com'),
)

# TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'
SERVER = 'local'
DEBUG = True

SITE_ID = 1

USE_I18N = True
USE_L10N = True

APPEND_SLASH = True

MEDIA_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, 'serve/media'))
STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, 'serve/static'))

TEMPLATE_DIRS = (
    os.path.abspath(os.path.join(PROJECT_PATH, 'templates'))
)

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

ADMIN_MEDIA_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, "static"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'wn*x-_*no&&(lfrt0s)ln8+rb5oopr8)gsc_&1kjii3!9cvyq_'

AUTH_PROFILE_MODULE = 'account.UserProfile'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
)

if SERVER is 'production':
    MIDDLEWARE_CLASSES += (
        'django.middleware.cache.FetchFromCacheMiddleware',
    )

MIDDLEWARE_CLASSES += (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'static_page.middleware.StaticpageFallbackMiddleware',
    'account.middleware.RegistrationMiddleware',
    "account.middleware.SocialAuthExceptionMiddleware",
)

if SERVER is 'production':
    MIDDLEWARE_CLASSES += (
        'etc.middleware.SetRemoteAddrFromForwardedFor',
    )

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
    'account.context_processors.profile',
    'messages.context_processors.inbox',
    'post.context_processors.count',
    'group.context_processors.count'
)

ROOT_URLCONF = 'urls'

LOGIN_REDIRECT_URL = '/account/home/'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.webdesign',
    'django.contrib.staticfiles',
    'account',
    'south',
    'social_auth',
    'common',
    'contact_form',
    'static_page',
    'ckeditor',
    'django_gravatar',
    'follow',
    'tagging',
    'gunicorn',
    'sorl.thumbnail',
    'south',
    'messages',
    'post',
    'django.contrib.humanize',
    'famdates.voting',
    'group',
    'news',
    'fileupload',
    'notification',
    'mailer',
    'zipdistance',
    'sf',
    'django_socketio',
    'chat',
    'events',
    'ajax_upload',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#        'LOCATION': '127.0.0.1:11211',
#        'TIMEOUT': 3600,
#    }
#}

# Email settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'noreply@simpleunion.com'
EMAIL_HOST_PASSWORD = 'n0reply321'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

# Django Social Auth

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
    'account.email_auth.EmailBackend',
)

SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook')
FACEBOOK_EXTENDED_PERMISSIONS = ['publish_stream', 'email']

#FACEBOOK_AUTH_EXTRA_ARGUMENTS = {'display': 'popup'}

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',

    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    'account.models.get_user_avatar',
)

SOCIAL_AUTH_UID_LENGTH = 222
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 200
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 135
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 125
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

ADMIN_MEDIA_PREFIX = '/static/'

LOGIN_URL = '/account/login/'
LOGOUT_URL = '/account/logout/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/account/home'
SOCIAL_AUTH_BACKEND_ERROR_URL = '/'

CKEDITOR_UPLOAD_PATH = MEDIA_ROOT

THUMBNAIL_DEBUG = False

NUMBER_POST = 10

LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/'

DEFAULT_FROM = 'noreply@simpleunion.com'
ITEM_PER_PAGE = 5
EVENTS_MAX_FUTURE_OCCURRENCES = 100

FACEBOOK_AUTH_EXTRA_ARGUMENTS = {'display': 'popup'}
