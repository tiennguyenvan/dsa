from invoice_repository import InvoiceRepository
from payment_repository import PaymentRepository


class BillingService:
    def __init__(self, invoices, payments):
        self._invoices = InvoiceRepository(invoices)
        self._payments = PaymentRepository(payments)

    def total_invoiced(self, customer_id):
        return sum(
            invoice["amount"]
            for invoice in self._invoices.for_customer(customer_id)
            if invoice["status"] != "CANCELLED"
        )

    def total_paid(self, customer_id):
        total = 0

        for payment in self._payments.completed_for_customer(customer_id):
            total += sum(
                allocation["amount"]
                for allocation in payment["allocations"]
            )

        return total
