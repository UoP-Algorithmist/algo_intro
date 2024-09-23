# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
stripe.api_key = "sk_test_26PHem9AhJZvU623DfE1x4sd"

stripe.Payout.create(
  amount=1000,
  currency="xaf",
)