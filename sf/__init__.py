from famdates.follow.models import *
from follow.signals import *
from famdates.notification.models import Notification
from django.contrib.sites.models import Site
from django.conf import settings
from famdates.contact_form.models import Contact


def new_follower(user, target, instance, **kwargs):
    try:
        current_domain = Site.objects.get_current().domain
        ctx = {
            'site_url': '%s://%s' % ('http', current_domain),
            'user': target.user,
            'follower': user,
        }

        print target.user.email
        if target.user.email:
            Notification.send(template='new_follower',
                              recipients=[target.user.email, ],
                              sent_from=settings.DEFAULT_FROM_EMAIL,
                              ctx=ctx)

    except Exception, e:
        pass #fail silently


followed.connect(new_follower)
