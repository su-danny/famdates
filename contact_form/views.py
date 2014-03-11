from django.core.context_processors import csrf
from django.contrib import messages
from django.shortcuts import render, render_to_response
from django.forms.models import modelformset_factory
from contact_form.models import Contact, ContactCategory

from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail

from django.template.loader import render_to_string
from django.contrib.sites.models import Site
import json
from contact_form.forms import ContactForm
from django.views.decorators.csrf import csrf_exempt
from django.template.base import Template
from django.template.context import Context
from famdates.mailer import send_html_mail


@csrf_exempt
def contact(request):
    c = {}
    c.update(csrf(request))

    contactFormSet = modelformset_factory(Contact)

    contactCategory = list(ContactCategory.objects.filter(is_active=True)[:1])

    if contactCategory:
        contactCategory = contactCategory[0]
        c.update({'contactCatetory': contactCategory})

    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact = contact.save()

            current_site = Site.objects.get_current()

            subject = Template(contactCategory.msg_subject).render(Context({'site': current_site}))

            # Email subject *must not* contain newlines
            subject = ''.join(subject.splitlines())

            message = Template(contactCategory.msg_body).render(Context(
                {'contact': contact,
                 'message': contact.message,
                 'site': current_site}));

            #           if contactCategory.msg_html_body:
            #               message = Template(contactCategory.msg_html_body).render(Context(
            #                                     {'contact': contact.name,
            #                                      'email': contact.email,
            #                                      'message': contact.message,
            #                                      'site': current_site }));

            send_html_mail(subject, message, message, settings.DEFAULT_FROM_EMAIL,
                           [email.strip() for email in contactCategory.recipients.split(',')])
            # send mail to contact person to inform them the email has been sent
            reply_subject = Template(contactCategory.reply_subject).render(Context({}))

            reply_message = Template(contactCategory.reply_body).render(Context({'contact': contact.name}))

            send_html_mail(reply_subject, reply_message, reply_message, settings.DEFAULT_FROM_EMAIL, [contact.email])

            if request.is_ajax():
                return HttpResponse(json.dumps({'success': True}), mimetype='application/json')
            else:
                return render(request, 'contact_form/message_sent.html')

        else:
            return HttpResponse(json.dumps({'success': False, 'errors': contact.errors}), mimetype='application/json')

    else:
        storage = messages.get_messages(request)
        storage.used = False
        c['contact'] = ContactForm()

    return render(request, "contact_form/contact.html", c)





