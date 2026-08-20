from inventory_repository import InventoryRepository
from order_repository import OrderRepository


class DispatchService:
    def __init__(self, orders, inventory):
        self._orders = OrderRepository(orders)
        self._inventory = InventoryRepository(inventory)

    def ready_order_ids(self, warehouse_id):
        return [
            order["id"]
            for order in self._orders.for_warehouse(warehouse_id)
            if order["status"] == "READY"
        ]

    def available_quantity(self, warehouse_id, sku):
        return self._inventory.quantity(warehouse_id, sku)

