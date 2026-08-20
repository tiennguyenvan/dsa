INVOICES = [
    {
        "id": "I2",
        "customer_id": "C1",
        "amount": 7000,
        "status": "OPEN",
        "due_date": "2026-08-15",
    },
    {
        "id": "I4",
        "customer_id": "C2",
        "amount": 8000,
        "status": "OPEN",
        "due_date": "2026-08-10",
    },
    {
        "id": "I1",
        "customer_id": "C1",
        "amount": 10000,
        "status": "OPEN",
        "due_date": "2026-08-01",
    },
    {
        "id": "I3",
        "customer_id": "C1",
        "amount": 5000,
        "status": "CANCELLED",
        "due_date": "2026-07-20",
    },
]


PAYMENTS = [
    {
        "id": "P1",
        "customer_id": "C1",
        "status": "COMPLETED",
        "allocations": [
            {"invoice_id": "I1", "amount": 4000},
        ],
    },
    {
        "id": "P2",
        "customer_id": "C1",
        "status": "PENDING",
        "allocations": [
            {"invoice_id": "I1", "amount": 2000},
        ],
    },
    {
        "id": "P3",
        "customer_id": "C1",
        "status": "COMPLETED",
        "allocations": [
            {"invoice_id": "I2", "amount": 8000},
        ],
    },
    {
        "id": "P4",
        "customer_id": "C2",
        "status": "COMPLETED",
        "allocations": [
            {"invoice_id": "I4", "amount": 3000},
        ],
    },
]
