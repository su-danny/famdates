#from django.http import HttpResponse, HttpBadRequest, Http404
from django.http import HttpResponse, Http404, HttpResponseRedirect, \
    HttpResponseForbidden
from django.conf import settings
import django.dispatch

import stripe

from signals import stripe_event
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict

try:
    import simplejson as json
except ImportError:
    import json

from tiger.models import Card
from tiger.forms import CreditCardForm


stripe_event = django.dispatch.Signal(providing_args=['event'])

STRIPE_DEBUG = getattr(settings, 'STRIPE_DEBUG', True)


def receive_webhook(request):
    if request.method != "POST":
        raise Http404
    data = json.loads(request.POST)
    # Confirm the event via stripe API
    event_id = data.get('id')
    if not event_id:
        return HttpBadRequest()
    event = stripe.Event.retrieve(event_id)

    # both live and test webhooks are sent to production applications
    if not STRIPE_DEBUG and not event.livemode:
        # it's a test and we're in production, ignore.
        return HttpResponse()
    stripe_event.send(sender=stripe.Event, event=event)
    return HttpResponse()


def get_card_form_data(card):
    """
    Field mapping
    
    fingerprint = models.CharField(max_length=20)
    last4 = models.CharField(max_length=4)
    type = models.CharField(max_length=16)
    exp_month = models.PositiveSmallIntegerField()
    exp_year = models.PositiveSmallIntegerField()
    address_line1 = models.CharField(max_length=100, blank=True, null=True)
    address_line2 = models.CharField(max_length=100, blank=True, null=True)
    address_state = models.CharField(max_length=20, blank=True, null=True)
    address_zip = models.CharField(max_length=10, blank=True, null=True)
    address_country = models.CharField(max_length=100, blank=True, null=True)
    
    
    card_type = forms.ChoiceField(choices=CREDIT_CARD_TYPE, label=_('Card Type'))
    card_number = PCISafeCharField(label=_('Card Number'))
    expiration_date = forms.CharField(widget=MonthYearWidget(), label=_('Expiration Date'))
    verification_number = PCISafeCharField(max_length=4, label=_('Verification Number'), 
                                           help_text="Last 3 digits on the back of your card. For AmEx, 4 digits on the first")
    card_name = forms.CharField(max_length=200, label=_('Name on Card'))
    billing_address = forms.CharField(max_length=200, label=_('Address'))
    billing_address_2 = forms.CharField(max_length=200, required=False, label=_('Address (line 2)'))
    city = forms.CharField(max_length=50, label=_('City'))
    state = forms.ChoiceField(choices=STATE_CHOICES, label=_('State'))
    zip = USZipCodeField(label=_('Zip'))
    stripe_token = forms.CharField(widget=forms.HiddenInput())
    """

    customer_info = card.get_stripe_customer()

    return {'card_number': card.last4,
            'card_type': card.type,
            'expiration_date': str(card.exp_month) + ' ' + str(card.exp_year),
            'stripe_token': card.fingerprint,
            'city': card.address_city,
            'billing_address': card.address_line1,
            'billing_address': card.address_line2,
            'billing_address': card.address_line2,
            'card_name': ''}


@login_required
def delete_card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    if card.user != request.user:
        return HttpResponseForbidden('Not allowed')

    card.delete()
    return HttpResponseRedirect('/credit_cards/manage')


@login_required
def make_default_card(request, card_id):
    card = get_object_or_404(Card, pk=card_id)

    if card.user != request.user:
        return HttpResponseForbidden('Not allowed')

    for card in Card.objects.filter(user=request.user):
        print card.id
        card.is_default = int(card_id) is card.id
        card.save()

    return HttpResponseRedirect('/credit_cards/manage/')


@login_required
def edit_card(request, template='credit_card/add_card.html'):
    ctx = {}
    card_dict = {}
    results = {'success': False}

    if request.method == 'POST':
        form = CreditCardForm(request.POST, initial=card_dict)
        if form.is_valid():
            results.update({'success': True})
            card = Card.objects.create(request.user, form.cleaned_data['stripe_token'])
            # update credit card billing info
            card.address_line1 = form.cleaned_data.get('billing_address')
            card.address_line2 = form.cleaned_data.get('billing_address_2')
            card.address_state = form.cleaned_data.get('state')
            card.address_zip = form.cleaned_data.get('zip')
            card.city = form.cleaned_data.get('city')
            card.save()

            # if card is the only card, make it the default
            if Card.objects.filter(user=request.user).count() == 1:
                card.is_default = True
                card.save()

            if request.is_ajax():
                return HttpResponse(json.dumps(results), mimetype='application/json')

        else:
            errors = form.errors_as_json(strip_tags=True)
            results.update(errors)
            if request.is_ajax():
                return HttpResponse(json.dumps(results), mimetype='application/json')
    else:
        form = CreditCardForm(initial=card_dict)

    ctx.update({'form': form})

    return render(request, template, ctx)


@login_required
def manage_cards(request, template='credit_card/cards.html'):
    user_cards = Card.objects.get_query_set().filter(user=request.user)

    return render(request, template, {'user_cards': user_cards})
    