# -*- coding: utf-8 -*-

#from social_auth.models import User
# mistaken django.contrib.auth.models User?
from django.contrib.auth.models import User

from models import GENDER_CHOICES


def get_username(details, user=None, *args, **kwargs):
    """Return an username for new user. Return current user username
    if user was given.
    """
    if user:
        return {
            'username': user.email
        }

    return {
        'username': details.get('email')
    }


def create_user(backend, details, response, uid, username, user=None, *args,
                **kwargs):
    """Create user. Depends on get_username pipeline."""

    if user:
        if not user.is_active:
            user.is_active = True
            user.save()

            profile = user.profile
            profile.reason = u''
            profile.save()
        return {
            'user': user
        }

    if not username:
        return None

    try:
        user = User.objects.get(email=username)
        created = False
    except User.DoesNotExist:
        user = User.objects.create(username=username, email=details.get('email'))
        created = True

    return {
        'user': user,
        'is_new': True if created else False
    }


def update_profile_details(backend, details, response, user, is_new=False, *args, **kwargs):
    """Update profile details using data from provider."""

    if is_new:
        user.set_unusable_password()
        user.save()

    profile = user.profile
    gender = response.get('gender', u'')
    if gender:
        if gender == 'male':
            profile.gender = GENDER_CHOICES[0][0]

        if gender == 'female':
            profile.gender = GENDER_CHOICES[1][0]

    facebook_uid = response.get('id', u'')
    if facebook_uid:
        profile.facebook_uid = facebook_uid
    profile.save()
