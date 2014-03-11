from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.loading import get_model
from django.conf import settings
from django.template.loader import get_template_from_string

from django.core.mail import send_mail
from mailer import send_mail as mailer_send_mail
from mailer import send_html_mail
from django.template import Context, Template
import datetime
from django.conf import settings
from django.contrib.sites.models import Site


class NotificationTemplate(models.Model):
    name = models.CharField(max_length=128, unique=True)
    created = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return self.name


class NotificationTemplateContent(models.Model):
    lang = models.CharField(choices=settings.LANGUAGES, max_length=10)
    body = models.TextField()
    html_body = models.TextField()
    subject = models.TextField(max_length=256)
    template = models.ForeignKey(NotificationTemplate, related_name='template_contents')
    updated_by = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        unique_together = ('lang', 'template')


class NotificationCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)


class Notification(models.Model):
    is_sent = models.BooleanField(default=False)
    category = models.ForeignKey(NotificationCategory, null=True, blank=True)
    recipients = models.CharField(max_length=1024)
    sent_from = models.CharField(max_length=256)
    subject = models.CharField(max_length=256)
    body = models.TextField()
    html_body = models.TextField()
    send_by_sms = models.BooleanField(default=False)
    send_by_email = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True, auto_now_add=True)
    send_on = models.DateTimeField('Scheduled to send on', auto_now_add=True) # not user for now
    sent_on = models.DateTimeField(null=True, blank=True)

    @classmethod
    def send(cls, *args, **kwargs):

        n = Notification()
        template = kwargs.get('template')
        language = kwargs.get('language', 'en')
        ctx = kwargs.get('ctx')
        recipients = kwargs.get('recipients')
        sent_from = kwargs.get('sent_from', settings.DEFAULT_FROM)

        n.send_by_mailer = kwargs.get('send_by_mailer', True)
        n.send_on_save = kwargs.get('send_on_save')

        if language == 'en-us':
            language = 'en'

        current_domain = Site.objects.get_current().domain
        ctx['site_url'] = '%s://%s' % ('http', current_domain)
        ctx['STATIC_URL'] = settings.STATIC_URL

        try:
            template = NotificationTemplateContent.objects.get(template__name=template, lang=language)

            n.subject = get_template_from_string(template.subject).render(Context(ctx))
            n.body = get_template_from_string(template.body).render(Context(ctx))
            n.html_body = get_template_from_string(template.html_body).render(Context(ctx))
            n.recipients = ','.join(recipients)
            n.sent_from = sent_from

        except NotificationTemplateContent.DoesNotExist:
            pass

        except Exception, e:
            print e

        n.save()

    def save(self):
        super(Notification, self).save()

        if self.is_sent:
            return

        if hasattr(self, 'send_by_mailer') and self.send_by_mailer:
            try:
                send_html_mail(self.subject, self.body, self.html_body, self.sent_from, self.recipients.split(','))
            except Exception, e:
                # log this error
                print str(e)

        if hasattr(self, 'send_on_save') and self.send_on_save:
            try:
                send_mail(self.subject, self.body, self.sent_from, self.recipients.split(','))
                self.is_sent = True
                self.sent_on = datetime.datetime.now()
                super(Notification, self).save()

            except Exception, e:
                print str(e)



                
