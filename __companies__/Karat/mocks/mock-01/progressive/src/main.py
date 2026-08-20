from billing_service import BillingService
from sample_data import INVOICES, PAYMENTS


service = BillingService(INVOICES, PAYMENTS)
print("Valids", service.outstanding_balance("C1"))
print("Valids", service.outstanding_balance("C2"))
print("Valids", service.outstanding_balance("C3"))
# print("C1 invoiced:", service.total_invoiced("C1"))
# print("C1 paid:", service.total_paid("C1"))
