# Karat-Style Progressive Feature Practice 02

This is a representative medium-hard, 35-minute real-world coding exercise. It is not an active Karat question.

## Scenario

You are extending a small billing system. All monetary values are integer cents:

- `10000` means `$100.00`.
- An invoice is money a customer owes.
- A payment allocation is the part of a payment assigned to one invoice.
- A `COMPLETED` payment affects balances; a `PENDING` payment does not.
- A `CANCELLED` invoice is not owed.

## Interview format

Requirements will be revealed progressively. Do not design speculative features.

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

The three baseline tests must pass before you begin.

## Feature 1 - Outstanding balance

Add this public method to `BillingService`:

```python
outstanding_balance(customer_id)
```

It returns the total amount the customer still owes.

Rules:

- Include only that customer's invoices.
- Ignore `CANCELLED` invoices.
- Subtract allocations from `COMPLETED` payments only.
- A single invoice's outstanding amount cannot be below zero.
- Unknown customers return `0`.
- Do not mutate invoices or payments.

Run:

```bash
python3 -m unittest discover -s src -p "*_tests.py" -v
```

Time budget: **8-10 minutes**.

When all tests pass, stop. Send your explanation and changed code before requesting Feature 2.
