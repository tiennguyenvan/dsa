import unittest

from billing_service import BillingService
from sample_data import INVOICES, PAYMENTS


class TestBillingServiceBaseline(unittest.TestCase):
    def setUp(self):
        self.service = BillingService(INVOICES, PAYMENTS)

    def test_total_invoiced_excludes_cancelled_invoices(self):
        self.assertEqual(self.service.total_invoiced("C1"), 17000)
        self.assertEqual(self.service.total_invoiced("C2"), 8000)

    def test_total_paid_uses_completed_payments(self):
        self.assertEqual(self.service.total_paid("C1"), 12000)
        self.assertEqual(self.service.total_paid("C2"), 3000)

    def test_unknown_customer_has_zero_totals(self):
        self.assertEqual(self.service.total_invoiced("UNKNOWN"), 0)
        self.assertEqual(self.service.total_paid("UNKNOWN"), 0)


if __name__ == "__main__":
    unittest.main()
