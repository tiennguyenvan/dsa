import unittest

from billing_service import BillingService
from sample_data import INVOICES, PAYMENTS


class TestOutstandingBalance(unittest.TestCase):
    def setUp(self):
        self.service = BillingService(INVOICES, PAYMENTS)

    def test_subtracts_only_completed_payment_allocations(self):
        self.assertEqual(self.service.outstanding_balance("C1"), 6000)

    def test_calculates_another_customer_independently(self):
        self.assertEqual(self.service.outstanding_balance("C2"), 5000)

    def test_unknown_customer_returns_zero(self):
        self.assertEqual(self.service.outstanding_balance("UNKNOWN"), 0)

    def test_does_not_allow_negative_invoice_balance(self):
        invoices = [
            {
                "id": "I9",
                "customer_id": "C9",
                "amount": 1000,
                "status": "OPEN",
                "due_date": "2026-08-01",
            }
        ]
        payments = [
            {
                "id": "P9",
                "customer_id": "C9",
                "status": "COMPLETED",
                "allocations": [
                    {"invoice_id": "I9", "amount": 1500},
                ],
            }
        ]

        service = BillingService(invoices, payments)

        self.assertEqual(service.outstanding_balance("C9"), 0)


if __name__ == "__main__":
    unittest.main()
