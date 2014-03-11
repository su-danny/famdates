import datetime
from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User
import stripe

from .models import Card, Invoice

if hasattr(settings, "STRIPE_SECRET_KEY") and \
        hasattr(settings, "STRIPE_PUB_KEY"):
    STRIPE_SECRET_KEY = settings.STRIPE_SECRET_KEY
    STRIPE_PUB_KEY = settings.STRIPE_PUB_KEY
    stripe.api_key = STRIPE_SECRET_KEY
else:
    raise ImproperlyConfigured("STRIPE_SECRET_KEY or STRIPE_PUB_KEY is not set.")

TEST_CARDS = {
    'Visa': ['4242424242424242', '4012888888881881'],
    'MasterCard': ['5555555555554444', '5105105105105100'],
    'American Express': ['378282246310005', '371449635398431'],
    'Discover': ['6011111111111117', '6011000990139424'],
    "Diner's Club": ['30569309025904', '38520000023237'],
    'JCB': ['3530111333300000', '3566002020360505']
}

# These simulate various error conditions
ERROR_CARDS = {
    # These will fail when creating a card token
    'address_line1': '4000000000000028',
    'address_zip': '4000000000000036',
    'cvc': '4000000000000101',
    # These will fail when a charge is attempted
    'charge_fail': '4000000000000341',
    'always_decline': '4000000000000002',
    'expired_card': '4000000000000069',
    'processing_error': '4000000000000119'
}

USER_DATA = [{
                 'username': 'testuser1',
                 'first_name': 'Test',
                 'last_name': 'User1',
                 'email': 'testuser1@example.com',
                 'password': 'password',
                 'card': {
                     'number': '4242424242424242',
                     'exp_month': 12,
                     'exp_year': datetime.datetime.now().year + 1,
                     'cvc': '123',
                     'address_line1': '123 Anywhere St',
                     'address_state': 'NY',
                     'address_zip': '12345',
                 }
             },
             {
                 'username': 'testuser2',
                 'first_name': 'Test',
                 'last_name': 'User2',
                 'email': 'testuser2@example.com',
                 'password': 'password',
                 'card': {
                     'number': '4242424242424242',
                     'exp_month': 12,
                     'exp_year': datetime.datetime.now().year + 1,
                     'cvc': '123',
                     'address_line1': '123 Anywhere St',
                     'address_state': 'NY',
                     'address_zip': '12345',
                 }
             }
]


def create_user_from_user_data(user_data):
    user = User.objects.create_user(user_data['username'],
                                    user_data['email'],
                                    user_data['password'])
    user.first_name = user_data['first_name']
    user.last_name = user_data['last_name']
    user.save()
    return user


def create_token_from_card_data(card_data):
    # Need to use the public key to create card tokens
    stripe.api_key = STRIPE_PUB_KEY
    token = stripe.Token.create(card=card_data)
    stripe.api_key = STRIPE_SECRET_KEY
    return token


class ModelTests(TestCase):
    def setUp(self):

        self.users = {}

        for user_data in USER_DATA:
            user = create_user_from_user_data(user_data)
            card_token = create_token_from_card_data(user_data['card'])
            self.users[user.username] = {
                'user': user,
                'card_token': card_token,
                'card_data': user_data['card']
            }

    def test_delete_from_stripe(self):
        userdata = self.users['testuser1']
        user = userdata['user']
        token = userdata['card_token']
        card = Card.objects.create(user, token.id)
        # There is a new stripe.Customer object
        try:
            customer = card.get_stripe_customer()
            self.assertEqual(user.email, customer.email)
        except stripe.InvalidRequestError:
            self.fail(msg="Stripe Customer did not exist after calling Card.objects.create.")
        deleted = card.delete_from_stripe()
        self.assertTrue(deleted)


    def test_create_card_for_user(self):
        userdata = self.users['testuser1']
        user = userdata['user']
        token = userdata['card_token']
        card = Card.objects.create(user, token.id)
        for attr in ['address_line1', 'address_zip', 'address_state', 'exp_month', 'exp_year']:
            self.assertEqual(getattr(card, attr), userdata['card_data'].get(attr))
            # test last4
        self.assertEqual('4242', card.last4)

        #cleanup
        card.delete_from_stripe()


class InvoiceTests(TestCase):
    def setUp(self):
        self.users = {}
        self._cards = []
        for user_data in USER_DATA:
            user = create_user_from_user_data(user_data)
            token = create_token_from_card_data(user_data['card'])
            card = Card.objects.create(user, token.id)
            self._cards.append(card)
            self.users[user.username] = user

    def tearDown(self):
        for card in self._cards:
            card.delete_from_stripe()


    def test_do_charge(self):
        user = self.users['testuser1']
        card = Card.objects.filter(user=user)[0]
        test_amount = 1500
        invoice = Invoice.objects.create(card, test_amount, "Test charge")
        paid = invoice._do_charge()
        self.assertTrue(paid)
        charge = invoice.get_stripe_charge()
        self.assertTrue(charge.paid)
        self.assertTrue(invoice.is_paid)

    def test_fail_cvc_check(self):
        user_data = {
            'username': 'testuser3',
            'first_name': 'Test',
            'last_name': 'User3',
            'email': 'testuser3@example.com',
            'password': 'password',
            'card': {
                'number': ERROR_CARDS['cvc'],
                'exp_month': 12,
                'exp_year': datetime.datetime.now().year + 1,
                'cvc': '123',
                'address_line1': '123 Anywhere St',
                'address_state': 'NY',
                'address_zip': '12345',
            }
        }
        user = create_user_from_user_data(user_data)
        token = create_token_from_card_data(user_data['card'])
        card = Card.objects.create(user, token.id)
        invoice = Invoice.objects.create(card, 1500, "Test charge")
        paid = invoice._do_charge()
        self.assertFalse(paid)
