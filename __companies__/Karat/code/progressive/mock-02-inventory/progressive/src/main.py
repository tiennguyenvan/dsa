from dispatch_service import DispatchService
from sample_data import INVENTORY, ORDERS


service = DispatchService(ORDERS, INVENTORY)
print("Ready W1 orders:", service.ready_order_ids("W1"))
print("W1 BOOK inventory:", service.available_quantity("W1", "BOOK"))

