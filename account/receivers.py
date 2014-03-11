# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=User, dispatch_uid='account.set_username')
def set_username(instance, **kwargs):
    ''' Set username as an email for a new user and if an email was changed. '''

    if instance.email and instance.id and instance.username != instance.email and not instance.is_superuser:
        has_group = instance.groups.filter(name=u'Usernames group').exists()

        if not has_group:
            instance.username = instance.email
