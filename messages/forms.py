import datetime
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

if "notification" in settings.INSTALLED_APPS:
    from notification import models as notification
else:
    notification = None

from messages.models import Message
from messages.fields import CommaSeparatedUserField
from notification.models import Notification


class ComposeForm(forms.Form):
    """
    A simple default form for private messages.
    """
    #    recipient = CommaSeparatedUserField(label=_(u"Recipient"))
    recipient = forms.ModelMultipleChoiceField(User.objects.all(), widget=forms.SelectMultiple(
        attrs={'data-placeholder': "Enter your friend's name", 'class': "chosen-form"}))
    subject = forms.CharField(label=_(u"Subject"), max_length=120, initial='Untitled', widget=forms.HiddenInput,
                              required=False)
    body = forms.CharField(label=_(u"Body"),
                           widget=forms.Textarea(attrs={'rows': '12', 'cols': '55'}))


    def __init__(self, *args, **kwargs):
        recipient_filter = kwargs.pop('recipient_filter', None)
        super(ComposeForm, self).__init__(*args, **kwargs)
        if recipient_filter is not None:
            self.fields['recipient']._recipient_filter = recipient_filter


    def save(self, sender, parent_msg=None):
        subject = self.cleaned_data['subject']
        body = self.cleaned_data['body']
        message_list = []
        for r in self.cleaned_data['recipient']:
            try:
                profile = r.get_profile()
                if profile.blocked_users.filter(id=sender.id).exists():
                    continue
            except:
                pass

            msg = Message(
                sender=sender,
                recipient=r,
                subject=subject,
                body=body,
            )
            if parent_msg is not None:
                msg.parent_msg = parent_msg
                parent_msg.replied_at = datetime.datetime.now()
                parent_msg.save()
            msg.save()
            message_list.append(msg)
            if notification:
                pass
            #                if parent_msg is not None:
            #                    notification.send([sender], "messages_replied", {'message': msg,})
            #                    notification.send([r], "messages_reply_received", {'message': msg,})
            #                else:
            #                    notification.send([sender], "messages_sent", {'message': msg,})
            #                    notification.send([r], "messages_received", {'message': msg,})
        return message_list
