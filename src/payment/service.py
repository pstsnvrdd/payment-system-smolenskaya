from src.payment.interfaces import PaymentProvider, PricingStrategy, PaymentEventListener

class PaymentService:
    def __init__(
        self,
        provider: PaymentProvider,
        pricing: PricingStrategy,
        listeners: list[PaymentEventListener]
    ):
        self.provider = provider
        self.pricing = pricing
        self.listeners = listeners or []

    def attach_listener(self, listener: PaymentEventListener):
        self.listeners.append(listener)
    def detach_listener(self, listener: PaymentEventListener):
        self.listeners.remove(listener)

    def process_payment(self, user_id: str, base_amount: int):
        final_amount = self.pricing.calculate(base_amount)
        context = {"user_id": user_id, "base_amount": base_amount, "final_amount": final_amount}
        try:
            txn_id = self.provider.charge(user_id, final_amount)
            context['txn_id'] = txn_id
            self._notify("payment_succeeded", context)
            return txn_id
        except Exception as e:
            context['error'] = str(e)
            self._notify("payment_failed", context)
            raise

    def _notify(self, event, data):
        for listener in self.listeners:
            listener.notify(event, data)