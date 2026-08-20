ORDERS = [
    {
        "id": "O-104",
        "warehouse_id": "W1",
        "status": "READY",
        "priority": "NORMAL",
        "created_at": "2026-08-19T09:00:00Z",
        "lines": [{"sku": "PEN", "quantity": 2}],
    },
    {
        "id": "O-101",
        "warehouse_id": "W1",
        "status": "READY",
        "priority": "HIGH",
        "created_at": "2026-08-19T08:00:00Z",
        "lines": [
            {"sku": "BOOK", "quantity": 2},
            {"sku": "PEN", "quantity": 1},
        ],
    },
    {
        "id": "O-103",
        "warehouse_id": "W1",
        "status": "READY",
        "priority": "HIGH",
        "created_at": "2026-08-19T08:30:00Z",
        "lines": [{"sku": "BOOK", "quantity": 4}],
    },
    {
        "id": "O-102",
        "warehouse_id": "W1",
        "status": "PENDING",
        "priority": "HIGH",
        "created_at": "2026-08-19T07:00:00Z",
        "lines": [{"sku": "BOOK", "quantity": 1}],
    },
    {
        "id": "O-201",
        "warehouse_id": "W2",
        "status": "READY",
        "priority": "NORMAL",
        "created_at": "2026-08-19T08:00:00Z",
        "lines": [{"sku": "BOOK", "quantity": 3}],
    },
]

INVENTORY = [
    {"warehouse_id": "W1", "sku": "BOOK", "quantity": 5},
    {"warehouse_id": "W1", "sku": "PEN", "quantity": 3},
    {"warehouse_id": "W2", "sku": "BOOK", "quantity": 2},
]

