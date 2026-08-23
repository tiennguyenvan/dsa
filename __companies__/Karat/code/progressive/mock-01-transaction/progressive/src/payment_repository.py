class PaymentRepository:
    def __init__(self, payments):
        self._payments = [self._copy(payment) for payment in payments]

    def completed_for_customer(self, customer_id):
        return [
            self._copy(payment)
            for payment in self._payments
            if payment["customer_id"] == customer_id
            and payment["status"] == "COMPLETED"
        ]

    def find_by_id(self, payment_id):
        for payment in self._payments:
            if payment["id"] == payment_id:
                return self._copy(payment)

        return None

    def add(self, payment):
        self._payments.append(self._copy(payment))

    @staticmethod
    def _copy(payment):
        result = dict(payment)
        result["allocations"] = [
            dict(allocation)
            for allocation in payment.get("allocations", [])
        ]
        return result
