from src.payment.interfaces import PricingStrategy

class TaxPricing(PricingStrategy):
    def __init__(self, tax_rate: float):
        self.tax_rate = tax_rate
    def calculate(self, base_amount: int) -> int:
        return int(base_amount * (1 + self.tax_rate))

class DiscountPricing(PricingStrategy):
    def __init__(self, discount_rate: float):
        self.discount_rate = discount_rate
    def calculate(self, base_amount: int) -> int:
        return int(base_amount * (1 - self.discount_rate))

class CombinedPricing(PricingStrategy):
    def __init__(self, strategies):
        self.strategies = strategies
    def calculate(self, base_amount: int) -> int:
        amount = base_amount
        for strat in self.strategies:
            amount = strat.calculate(amount)
        return amount