PRODUCTS = [
    {
        "id": "P1",
        "price": 10000,
        "default_discount_percent": 10,
    },
    {
        "id": "P2",
        "price": 2599,
        "default_discount_percent": 0,
    },
]

DISCOUNT_RULES = [
    {"product_id": "P1", "segment": "EMPLOYEE", "percent": 25},
    {"product_id": "P1", "segment": "PARTNER", "percent": 0},
    {"product_id": "P2", "segment": "EMPLOYEE", "percent": 10},
]

