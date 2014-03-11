from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
import datetime
from django.contrib.sites.models import Site
from famdates.notification.models import Notification


class Group(models.Model):
    name = models.CharField(max_length=200)
    group_type = models.CharField(max_length=200, default='')
    owner = models.ForeignKey(User, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    default_image = models.ImageField(upload_to='groups', blank=True, null=True)
    about = models.TextField(null=True, blank=True)
    is_private = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Group')
        verbose_name_plural = _('Groups')
        ordering = ('name',)

    def get_member_count(self):
        return UserGroup.objects.filter(group=self, invitation_accepted=True).count()

    def send_inivitation(self, request, name_or_email):
        if not self.pk:
            self.save()

        if '@' in name_or_email:
            user = User.objects.filter(email=name_or_email)[:1]
            if user:
                user = user[0]
            else:
                return False
        else:
            first_name, last_name = tuple([name.lower() for name in name_or_email.split()])
            user = User.objects.filter(first_name__icontains=first_name, last_name__icontains=last_name)[:1]
            if user: user = user[0]

        user_group, created = UserGroup.objects.get_or_create(user=user, group=self)
        #        if user_group.invitation_accepted:
        #            return False

        user_group.generate_secret_code()
        user_group.invitation_accepted = False
        user_group.save()
        #        current_site = Site.objects.get_current()

        #        send_mail('Group Invitation',
        #                  """
        #                      You have a group invitation from %s
        #                      Accept this by clicking on http://%/group/accept/%s
        #
        #                  """ % (self.user.get_profile.get_pretty_name(), current_site.domain, user_group.invitation_code),
        #                  'noreplya@simpleunion.com',
        #                  [user.email,], fail_silently=False)

        Notification.send(template="group_invite", recipients=[user.email, ],
                          ctx={'group': self, 'user_group': user_group, 'user': user})

        return True


class UserGroup(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    invitation_code = models.CharField(max_length=100, unique=True)
    invitation_accepted = models.BooleanField(default=True)

    class Meta:
        unique_together = ("user", "group")

    @classmethod
    def user_accept(cls, code):
        pass

    def generate_secret_code(self):
        self.invitation_code = str(hash(str(datetime.datetime.now()) + 'seCr3t')).replace('-', '')
        self.save()


class Message(models.Model):
    author = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    content = models.CharField(max_length=200)
    parent = models.ForeignKey('self', related_name='reply_messages', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)
    
    
    
    