class InventoryRepository:
    def __init__(self, inventory):
        self._inventory = [dict(item) for item in inventory]

    def for_warehouse(self, warehouse_id):
        return [
            dict(item)
            for item in self._inventory
            if item["warehouse_id"] == warehouse_id
        ]

    def quantity(self, warehouse_id, sku):
        for item in self._inventory:
            if item["warehouse_id"] == warehouse_id and item["sku"] == sku:
                return item["quantity"]

        return 0

