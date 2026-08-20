# Karat-Style Debugging Practice 02

This is a representative IC3-IC4, 15-minute real-world debugging exercise. It is not an active Karat question.

## Scenario

An online store applies percentage discounts to product prices.

Business rules:

- A segment-specific discount overrides the product's default discount.
- A segment-specific discount may explicitly be `0`, meaning no discount.
- If no segment-specific rule exists, use the product's default discount.
- Prices are integer cents and the final price is rounded down to whole cents.
- Unknown products return `None`.

The implementation has a bug. Some existing tests fail.

## Interview rules

Set a 15-minute timer and behave as if an interviewer is watching:

1. Run all tests to establish the baseline.
2. Read the tests and trace the code across the files.
3. Explain your observations and hypothesis aloud.
4. State the root cause before editing.
5. Make the smallest correct fix.
6. Run the complete test suite again.
7. Summarize the fix and runtime complexity.

Do not modify the tests.

## Run

```bash
python3 -m unittest discover -s src -p "tests.py" -v
```

You can also use **Terminal > Run Task > Run Karat Tests**.

## What to submit for evaluation

- Root-cause explanation
- Changed lines only
- Final test output
- Time taken

