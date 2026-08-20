from invoice_repository import InvoiceRepository
from payment_repository import PaymentRepository
from collections import Counter


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

    def outstanding_balance(self, customer_id):
        """
        [ ] Include only that customer's non-`CANCELLED` invoices.
        [ ] Subtract allocations from `COMPLETED` payments only.
        [ ] A "SINGLE" invoice's outstanding amount cannot be below zero.
        [v] Unknown customers return `0`.
        [ ] Do not mutate invoices or payments.
        """
        validInvoices = [
            invoice
            for invoice in self._invoices.for_customer(customer_id)
            if invoice["status"] != "CANCELLED"
        ]
        if not validInvoices:
            return 0

        sumByInvoiceIds = Counter()
        for invoice in validInvoices:
            sumByInvoiceIds[invoice['id']] += invoice['amount']

        # print(validInvoicesIds)
        for payment in self._payments.completed_for_customer(customer_id):
            for allocation in payment["allocations"]:
                id = allocation['invoice_id']
                if id not in sumByInvoiceIds:
                    continue
                sumByInvoiceIds[id] = max(
                    0, sumByInvoiceIds[id] - allocation['amount']
                )

        return sum(amount for amount in sumByInvoiceIds.values())
