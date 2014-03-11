DEBUG = True
SERVER = 'local'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sf',
        'USER': 'root',
        'PASSWORD': 'root123',
    }
}

MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/media/admin/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

FACEBOOK_APP_ID = '499006443500081'
FACEBOOK_API_KEY = '499006443500081'
FACEBOOK_API_SECRET = '94116da3bc57086e13adc77e27ae6741'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False