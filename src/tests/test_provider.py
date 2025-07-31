import pytest
from src.payment.providers import StripeProvider, PayPalProvider, FakePaymentProvider

def test_stripe_success():
    provider = StripeProvider()
    assert provider.charge("u", 200).startswith("stripe_txn")

def test_stripe_failure():
    provider = StripeProvider()
    with pytest.raises(Exception):
        provider.charge("u", 50)

def test_paypal_success():
    provider = PayPalProvider()
    assert provider.charge("u", 500).startswith("paypal_txn")

def test_paypal_failure():
    provider = PayPalProvider()
    with pytest.raises(Exception):
        provider.charge("u", 50)

def test_fake_success():
    provider = FakePaymentProvider()
    assert provider.charge("u", 123).startswith("fake_txn")

def test_fake_failure():
    provider = FakePaymentProvider()
    with pytest.raises(Exception):
        provider.charge("u", 666)