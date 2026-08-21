import unittest

from pricing_service import PricingService
from sample_data import DISCOUNT_RULES, PRODUCTS


class TestPricingService(unittest.TestCase):
    def setUp(self):
        self.service = PricingService(PRODUCTS, DISCOUNT_RULES)

    def test_uses_segment_discount_when_present(self):
        self.assertEqual(self.service.final_price("P1", "EMPLOYEE"), 7500)

    def test_uses_default_when_segment_rule_is_absent(self):
        self.assertEqual(self.service.final_price("P1", "PUBLIC"), 9000)

    def test_explicit_zero_segment_discount_overrides_default(self):
        self.assertEqual(self.service.final_price("P1", "PARTNER"), 10000)

    def test_rounds_down_to_whole_cents(self):
        self.assertEqual(self.service.final_price("P2", "EMPLOYEE"), 2339)

    def test_unknown_product_returns_none(self):
        self.assertIsNone(self.service.final_price("UNKNOWN", "PUBLIC"))


if __name__ == "__main__":
    unittest.main()

