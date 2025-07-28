import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_stripe_session(item):
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': item.name},
                    'unit_amount': item.price,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=f"{settings.SITE_URL}/success/",
            cancel_url=f"{settings.SITE_URL}/cancel/",
        )
        return session.id
    except stripe.error.StripeError as e:
        print(f"Stripe error: {e}")
        return None