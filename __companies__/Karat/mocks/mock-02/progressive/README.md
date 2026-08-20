# Karat-Style Progressive Feature Practice 02

This is a representative IC3-IC4, 25-minute real-world coding exercise. It is not an active Karat question.

## Scenario

You are extending a warehouse dispatch system. Each order contains one or more product lines, and inventory is tracked per warehouse.

## Interview format

Requirements are revealed progressively. Do not design speculative features.

For each feature:

1. Restate the requirement.
2. Clarify inputs, outputs, and edge cases.
3. Explain the integration point and plan.
4. Implement the simplest working version.
5. Run all tests.
6. Summarize correctness and complexity.

## Setup

Open this folder in VS Code. No third-party packages are required.

Verify the existing code first:

```bash
python3 -m unittest discover -s src -p "baseline_tests.py" -v
```

The four baseline tests must pass before you begin.

## Feature 1 - Dispatch plan

Add this public method to `DispatchService`:

```python
dispatchable_order_ids(warehouse_id)
```

It returns the order IDs that can be fully dispatched from the warehouse's current inventory.

Rules:

- Consider only `READY` orders for the requested warehouse.
- Process `HIGH` priority orders before `NORMAL` priority orders.
- Within the same priority, process older `created_at` values first; use order ID as the final tie-breaker.
- An order is dispatchable only if every line can be filled.
- Inventory is shared across orders. Reserve inventory in the processing order for each dispatchable order.
- If an order cannot be fully filled, skip it and do not consume any inventory for it.
- Multiple lines for the same SKU in one order must be combined before checking inventory.
- Unknown warehouses return an empty list.
- Do not mutate orders or inventory.

Return IDs in processing order.

Run:

```bash
python3 -m unittest discover -s src -p "*_tests.py" -v
```

Time budget: **25 minutes**.

When all tests pass, summarize your approach, correctness, and time and space complexity.

