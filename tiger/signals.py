import django.dispatch

# Signal sent when a Stripe webhook POST is received
stripe_event = django.dispatch.Signal(providing_args=['event'])

# Signal sent when an Invoice is successfully paid.
invoice_paid = django.dispatch.Signal(providing_args=['charge'])

# Signal sent when an charge is attempted but returns charge.paid = False
invoice_charge_failure = django.dispatch.Signal(providing_args=['charge'])