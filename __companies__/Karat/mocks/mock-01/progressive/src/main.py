from billing_service import BillingService
from sample_data import INVOICES, PAYMENTS


service = BillingService(INVOICES, PAYMENTS)
print("C1 invoiced:", service.total_invoiced("C1"))
print("C1 paid:", service.total_paid("C1"))
