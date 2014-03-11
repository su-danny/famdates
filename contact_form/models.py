from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)


class ContactCategory(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    contact_page_content = models.TextField(null=True, blank=True)

    send_reply = models.BooleanField(default=True)
    reply_subject = models.CharField(max_length=200, null=True, blank=True)
    reply_body = models.TextField(null=True, blank=True)

    recipients = models.CharField(max_length=200, verbose_name='The list of emails will receive the submit')
    msg_subject = models.CharField(max_length=200)
    msg_body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

