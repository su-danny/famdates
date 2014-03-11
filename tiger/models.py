import datetime
from decimal import Decimal
from django.db import models
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save

import stripe

from signals import invoice_paid, invoice_charge_failure

STRIPE_MINIMUM_CHARGE = 50 # in cents

if hasattr(settings, "STRIPE_SECRET_KEY"):
    stripe.api_key = settings.STRIPE_SECRET_KEY
else:
    raise ImproperlyConfigured("STRIPE_SECRET_KEY is not set.")


def set_stripe_api_key(public=False):
    """
    Convenience function for setting stripe's API key.
    
    Pass `public=True` to use the public API key, for creating card tokens.
    """
    if public:
        if hasattr(settings, "STRIPE_PUB_KEY"):
            stripe.api_key = settings.STRIPE_PUB_KEY
        else:
            raise ImproperlyConfigured("STRIPE_PUB_KEY is not set")
    stripe.api_key = settings.STRIPE_SECRET_KEY


class CardManager(models.Manager):
    def get_query_set(self, *args, **kwargs):
        return super(CardManager, self).get_query_set(*args, **kwargs).filter(deleted=None)

    def deleted(self, *args, **kwargs):
        return super(CardManager, self).get_query_set(*args, **kwargs).exclude(deleted=None)

    def all(self, *args, **kwargs):
        return super(CardManager, self).get_query_set(*args, **kwargs)

    def create(self, user, stripe_token):
        """
        Create a Card for the given User, with a Stripe token
        created with stripe.js.
        """

        stripe_customer = stripe.Customer.create(
            description=user.get_full_name(),
            card=stripe_token,
            email=user.email
        )

        card_data = stripe_customer.active_card.to_dict()
        kwargs = {arg: card_data.get(arg) for arg in
                  ['fingerprint', 'last4', 'type', 'exp_month', 'exp_year',
                   'address_line1', 'address_line2', 'address_state', 'address_zip',
                   'address_country']}
        kwargs['user'] = user
        kwargs['stripe_id'] = stripe_customer.id
        card = Card(**kwargs)
        card.save()
        return card


class Card(models.Model):
    # stripe.Customer
    stripe_id = models.CharField(max_length=25)

    # stripe.Customer.active_card
    fingerprint = models.CharField(max_length=20)
    last4 = models.CharField(max_length=4)
    type = models.CharField(max_length=16)
    exp_month = models.PositiveSmallIntegerField()
    exp_year = models.PositiveSmallIntegerField()
    address_line1 = models.CharField(max_length=100, blank=True, null=True)
    address_line2 = models.CharField(max_length=100, blank=True, null=True)
    address_state = models.CharField(max_length=20, blank=True, null=True)
    address_zip = models.CharField(max_length=10, blank=True, null=True)
    address_city = models.CharField(max_length=10, blank=True, null=True)
    address_country = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(User, related_name='credit_cards')

    deleted = models.DateTimeField(blank=True, null=True)
    is_default = models.BooleanField(default=False)

    objects = CardManager()

    def __unicode__(self):
        return "%s **%s" % (self.type, self.last4)

    @property
    def get_billing_address(self):
        if self.address_line2:
            return "%s %s %s %s" % (
            self.address_line1 or '', self.address_state or '', self.address_zip or '', self.address_country or '')
        else:
            return "%s %s %s %s %s" % (
            self.address_line1 or '', self.address_line2 or '', self.address_state or '', self.address_zip or '',
            self.address_country or '')

    @property
    def is_active(self):
        return self.deleted is None

    def get_stripe_customer(self):
        return stripe.Customer.retrieve(self.stripe_id)

    def delete_from_stripe(self):
        if self.deleted is None:
            stripe_customer = self.get_stripe_customer()
            response = stripe_customer.delete()
            if response.deleted:
                self.deleted = datetime.datetime.now()
                self.save()
                return True
        return False

    def delete(self, force=False):
        self.delete_from_stripe()
        if force:
            super(Card, self).delete()

    @classmethod
    def get_default_for_user(cls, user):
        cards = cls.objects.filter(user=user)
        if cards:
            for card in cards:
                if card.is_default:
                    return card
            return cards[0]
        return None


def get_all_stripe_customers(cls):
    """
    Blocking API call(s) to return a list of all stripe.Customer objects (not tiger.Customer).
    """
    customers_per_api_call = 100 # max 100
    offset = 0
    customers = []
    get_more = True
    while get_more:
        cu = stripe.Customer.all(count=100, offset=offset)['data']
        if len(cu) == 0:
            get_more = False
        else:
            offset += customers_per_api_call
            customers.append(cu)
    return customers


class InvoiceManager(models.Manager):
    def create(self, card, amount, description=None):
        if not card.is_active:
            raise ValueError("Cannot create an Invoice with an inactive Card")
        return super(InvoiceManager, self).create(
            card=card,
            amount=amount,
            description=description
        )


class Invoice(models.Model):
    """
    Create an Invoice to charge a Card.
    """
    amount = models.PositiveIntegerField(validators=[MinValueValidator(STRIPE_MINIMUM_CHARGE)],
                                         help_text='Invoice amount, in cents')
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    submitted = models.DateTimeField(blank=True, null=True,
                                     help_text='When this invoice was submitted to Stripe')
    charge_id = models.CharField(max_length=25, blank=True, null=True,
                                 help_text='The stripe.Charge ID associated with this transaction.')
    charge_attempts = models.TextField(help_text='space separated list of unsuccessful charge attempts')
    card = models.ForeignKey(Card, help_text="The card to charge")

    objects = InvoiceManager()

    def save(self, *args, **kwargs):
        if type(self.amount) == Decimal:
            # Convert a decimal in dollars to an int representing cents
            decimal_cents = self.amount.quantize(Decimal('.01')) * 100
            self.amount = int(decimal_cents.to_integral_value().to_eng_string())
            if self.amount < STRIPE_MINIMUM_CHARGE:
                raise ValidationError("Invoice amount must be greater than %d" % STRIPE_MINIMUM_CHARGE)
        super(Invoice, self).save(*args, **kwargs)

    def submit_for_payment(self):
        """
        Function for calling classes to request payment.
        """
        # TODO: Make this an asyncronous task
        if not self.is_paid:
            self._do_charge()

    def _do_charge(self):
        """
        Charges the card by the amount. Returns True if payment is successful,
        False otherwise.
        
        Sends `invoice_paid` signal on success, `invoice_charge_failure` on failure.
        """
        kwargs = {
            'amount': self.amount,
            'currency': 'usd',
            'customer': self.card.stripe_id,
        }
        if self.description:
            kwargs['description'] = self.description
        charge = stripe.Charge.create(**kwargs)
        if charge.paid:
            self.charge_id = charge.id
            invoice_paid.send(sender=self, charge=charge)
            return True
        else:
            invoice_charge_failure.send(sender=self, charge=charge)
        return False

    @property
    def is_paid(self):
        if self.charge_id:
            return True
        return False

    def get_stripe_charge(self):
        """
        Retrieve the associated stripe.Charge via the Stripe API.
        
        Returns None if the Invoice has not yet been charged.
        """
        if self.charge_id:
            return stripe.Charge.retrieve(self.charge_id)
        return None
        

