class InvoiceRepository:
    def __init__(self, invoices):
        self._invoices = [dict(invoice) for invoice in invoices]

    def for_customer(self, customer_id):
        return [
            dict(invoice)
            for invoice in self._invoices
            if invoice["customer_id"] == customer_id
        ]

    def find_by_id(self, invoice_id):
        for invoice in self._invoices:
            if invoice["id"] == invoice_id:
                return dict(invoice)

        return None
