from abc import ABC, abstractmethod

class PaymentProvider(ABC):
    @abstractmethod
    def charge(self, user_id: str, amount_cents: int) -> str:
        pass

class PricingStrategy(ABC):
    @abstractmethod
    def calculate(self, base_amount: int) -> int:
        pass

class PaymentEventListener(ABC):
    @abstractmethod
    def notify(self, event: str, data: dict):
        pass