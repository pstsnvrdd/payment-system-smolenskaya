from src.payment.pricing import TaxPricing, DiscountPricing, CombinedPricing

def test_tax_pricing():
    strat = TaxPricing(0.10)
    assert strat.calculate(1000) == 1100

def test_discount_pricing():
    strat = DiscountPricing(0.20)
    assert strat.calculate(1000) == 800

def test_combined_pricing():
    strat = CombinedPricing([TaxPricing(0.10), DiscountPricing(0.20)])
    assert strat.calculate(1000) == 880 # 1000*1.1=1100 *0.8 = 880