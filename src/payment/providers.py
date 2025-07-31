from src.payment.interfaces import PaymentProvider

# Stripe Adapter
class StripeProvider(PaymentProvider):
    def charge(self, user_id: str, amount_cents: int) -> str:
        # Simulate Stripe SDK
        if amount_cents < 100:
            raise Exception("Stripe: Amount too low")
        return f"stripe_txn_{user_id}_{amount_cents}"

# PayPal Adapter
class PayPalProvider(PaymentProvider):
    def charge(self, user_id: str, amount_cents: int) -> str:
        # Simulate PayPal SDK
        if amount_cents < 100:
            raise Exception("PayPal: Amount too low")
        return f"paypal_txn_{user_id}_{amount_cents}"

# Fake Provider for testing/fallback
class FakePaymentProvider(PaymentProvider):
    def charge(self, user_id: str, amount_cents: int) -> str:
        if amount_cents == 666:
            raise Exception("FakeProvider: Simulated failure")
        return f"fake_txn_{user_id}_{amount_cents}"