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

    def _ready_sorted_orders(self, warehouse_id):
        orders = [
            order
            for order in self._orders.for_warehouse(warehouse_id)
            if order["status"] == "READY"
        ]
        priority_rank = {"HIGH": 0, "NORMAL": 1}
        return sorted(orders, key=lambda o: (
            priority_rank[o["priority"]], o["created_at"], o["id"]
        ))

    def _combined_order_skus(self, order_lines):
        order_sku_qty = dict()
        for line in order_lines:
            sku, qty = line["sku"], line["quantity"]
            if sku not in order_sku_qty:
                order_sku_qty[sku] = 0
            order_sku_qty[sku] += qty
        return order_sku_qty

    def _try_fullfill_reverse_if_not(self, inv_sku_qty, order_sku_qty):
        fulfilled = True
        for sku in order_sku_qty:
            if sku not in inv_sku_qty or inv_sku_qty[sku] < order_sku_qty[sku]:
                fulfilled = False
                break

        if not fulfilled:
            return False
        for sku in order_sku_qty:
            inv_sku_qty[sku] -= order_sku_qty[sku]
        return True

    def dispatchable_order_ids(self, warehouse_id):
        warehouse_inventory = self._inventory.for_warehouse(warehouse_id)
        dispatchable_ids = []
        if not warehouse_inventory:
            return dispatchable_ids

        inv_sku_qty = dict()
        for inventory in warehouse_inventory:
            inv_sku_qty[inventory["sku"]] = inventory["quantity"]

        for order in self._ready_sorted_orders(warehouse_id):
            order_sku_qty = self._combined_order_skus(order['lines'])
            if not self._try_fullfill_reverse_if_not(inv_sku_qty, order_sku_qty):
                continue

            dispatchable_ids.append(order["id"])
        return dispatchable_ids
