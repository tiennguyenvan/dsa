from pricing_service import PricingService
from sample_data import DISCOUNT_RULES, PRODUCTS


service = PricingService(PRODUCTS, DISCOUNT_RULES)
print("Employee price:", service.final_price("P1", "EMPLOYEE"))
print("Partner price:", service.final_price("P1", "PARTNER"))

