class OrderRepository:
    def __init__(self, orders):
        self._orders = [self._copy(order) for order in orders]

    def for_warehouse(self, warehouse_id):
        return [
            self._copy(order)
            for order in self._orders
            if order["warehouse_id"] == warehouse_id
        ]

    def find_by_id(self, order_id):
        for order in self._orders:
            if order["id"] == order_id:
                return self._copy(order)

        return None

    @staticmethod
    def _copy(order):
        result = dict(order)
        result["lines"] = [dict(line) for line in order.get("lines", [])]
        return result

