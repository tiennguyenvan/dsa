import unittest

from dispatch_service import DispatchService
from sample_data import INVENTORY, ORDERS


class TestDispatchServiceBaseline(unittest.TestCase):
    def setUp(self):
        self.service = DispatchService(ORDERS, INVENTORY)

    def test_lists_ready_orders_for_warehouse(self):
        self.assertEqual(
            self.service.ready_order_ids("W1"),
            ["O-104", "O-101", "O-103"],
        )

    def test_does_not_mix_warehouses(self):
        self.assertEqual(self.service.ready_order_ids("W2"), ["O-201"])

    def test_returns_inventory_quantity(self):
        self.assertEqual(self.service.available_quantity("W1", "BOOK"), 5)

    def test_unknown_inventory_returns_zero(self):
        self.assertEqual(self.service.available_quantity("W1", "UNKNOWN"), 0)


if __name__ == "__main__":
    unittest.main()

