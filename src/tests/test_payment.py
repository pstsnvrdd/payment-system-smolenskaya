import logging
import pytest
from src.payment.providers import FakePaymentProvider
from src.payment.pricing import TaxPricing
from src.payment.observer import LoggingListener
from src.payment.service import PaymentService

def test_payment_success():
    provider = FakePaymentProvider()
    pricing = TaxPricing(0.05)
    listener = LoggingListener()
    service = PaymentService(provider, pricing, [listener])
    txn_id = service.process_payment("u1", 1000)  # 1000 * 1.05 = 1050
    assert txn_id == "fake_txn_u1_1050"

def test_payment_failure():
    provider = FakePaymentProvider()
    pricing = TaxPricing(0.0)  # 666 * 1.0 = 666
    listener = LoggingListener()
    service = PaymentService(provider, pricing, [listener])
    with pytest.raises(Exception) as exc:
        service.process_payment("u1", 666)
    assert "Simulated failure" in str(exc.value)