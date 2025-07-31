from fastapi import FastAPI, HTTPException
from src.config import Config
from src.payment.providers import StripeProvider, PayPalProvider, FakePaymentProvider
from src.payment.pricing import TaxPricing, DiscountPricing, CombinedPricing
from src.payment.observer import LoggingListener, AdminAlertListener
from src.payment.service import PaymentService

import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

def get_provider():
    if Config.payment_provider == "stripe":
        return StripeProvider()
    elif Config.payment_provider == "paypal":
        return PayPalProvider()
    elif Config.payment_provider == "fake":
        return FakePaymentProvider()
    else:
        raise Exception("Unknown provider")

def get_pricing():
    # Compose strategies
    strategies = []
    if Config.tax_rate > 0:
        strategies.append(TaxPricing(Config.tax_rate))
    if Config.discount_rate > 0:
        strategies.append(DiscountPricing(Config.discount_rate))
    return CombinedPricing(strategies) if strategies else (lambda x: x)

listeners = [LoggingListener(), AdminAlertListener()]
payment_service = PaymentService(
    provider=get_provider(),
    pricing=get_pricing(),
    listeners=listeners
)

@app.post("/pay/")
def make_payment(user_id: str, amount: int):
    try:
        txn_id = payment_service.process_payment(user_id, amount)
        return {"status": "success", "txn_id": txn_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))