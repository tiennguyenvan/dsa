import copy
import unittest

from dispatch_service import DispatchService
from sample_data import INVENTORY, ORDERS


class TestDispatchableOrders(unittest.TestCase):
    def test_prioritizes_orders_and_shares_inventory(self):
        service = DispatchService(ORDERS, INVENTORY)

        self.assertEqual(
            service.dispatchable_order_ids("W1"),
            ["O-101", "O-104"],
        )

    def test_skipped_order_does_not_consume_inventory(self):
        orders = [
            self._order("O-1", "HIGH", "08:00", [{"sku": "A", "quantity": 6}]),
            self._order("O-2", "NORMAL", "09:00", [{"sku": "A", "quantity": 4}]),
        ]
        inventory = [{"warehouse_id": "W1", "sku": "A", "quantity": 5}]

        service = DispatchService(orders, inventory)

        self.assertEqual(service.dispatchable_order_ids("W1"), ["O-2"])

    def test_combines_duplicate_sku_lines(self):
        orders = [
            self._order(
                "O-1",
                "HIGH",
                "08:00",
                [
                    {"sku": "A", "quantity": 3},
                    {"sku": "A", "quantity": 3},
                ],
            ),
            self._order("O-2", "NORMAL", "09:00", [{"sku": "A", "quantity": 5}]),
        ]
        inventory = [{"warehouse_id": "W1", "sku": "A", "quantity": 5}]

        service = DispatchService(orders, inventory)

        self.assertEqual(service.dispatchable_order_ids("W1"), ["O-2"])

    def test_uses_created_at_then_id_as_tie_breakers(self):
        orders = [
            self._order("O-3", "HIGH", "09:00", [{"sku": "A", "quantity": 1}]),
            self._order("O-2", "HIGH", "08:00", [{"sku": "A", "quantity": 1}]),
            self._order("O-1", "HIGH", "08:00", [{"sku": "A", "quantity": 1}]),
        ]
        inventory = [{"warehouse_id": "W1", "sku": "A", "quantity": 2}]

        service = DispatchService(orders, inventory)

        self.assertEqual(service.dispatchable_order_ids("W1"), ["O-1", "O-2"])

    def test_ignores_non_ready_orders_and_other_warehouses(self):
        orders = [
            self._order("O-1", "HIGH", "08:00", [{"sku": "A", "quantity": 1}], status="PENDING"),
            self._order("O-2", "HIGH", "08:00", [{"sku": "A", "quantity": 1}], warehouse_id="W2"),
        ]
        inventory = [
            {"warehouse_id": "W1", "sku": "A", "quantity": 2},
            {"warehouse_id": "W2", "sku": "A", "quantity": 2},
        ]

        service = DispatchService(orders, inventory)

        self.assertEqual(service.dispatchable_order_ids("W1"), [])

    def test_unknown_warehouse_returns_empty_list(self):
        service = DispatchService(ORDERS, INVENTORY)

        self.assertEqual(service.dispatchable_order_ids("UNKNOWN"), [])

    def test_does_not_mutate_inputs(self):
        orders = copy.deepcopy(ORDERS)
        inventory = copy.deepcopy(INVENTORY)
        expected_orders = copy.deepcopy(orders)
        expected_inventory = copy.deepcopy(inventory)
        service = DispatchService(orders, inventory)

        service.dispatchable_order_ids("W1")

        self.assertEqual(orders, expected_orders)
        self.assertEqual(inventory, expected_inventory)

    @staticmethod
    def _order(
        order_id,
        priority,
        created_at,
        lines,
        status="READY",
        warehouse_id="W1",
    ):
        return {
            "id": order_id,
            "warehouse_id": warehouse_id,
            "status": status,
            "priority": priority,
            "created_at": created_at,
            "lines": lines,
        }


if __name__ == "__main__":
    unittest.main()

