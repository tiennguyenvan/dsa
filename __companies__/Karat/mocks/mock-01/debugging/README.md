# Karat-Style Debugging Practice 01

This is a representative 15-minute real-world debugging exercise. It is not an active Karat interview question.

## Scenario

A portfolio owns stock positions. Stock quotes arrive in no guaranteed order.

Business rules:

- A position is the number of shares currently owned.
- A quote is a stock price recorded at a specific time.
- Times may use either `H:MM` or `HH:MM`.
- For each symbol, use the latest quote at or before `as_of`.
- Ignore positions that have no available quote.

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

## Open in VS Code

Open this folder as the VS Code workspace. No third-party packages are required.

Run the tests from the terminal:

```bash
python3 -m unittest discover -s src -p "tests.py" -v
```

You can also use **Terminal > Run Task > Run Karat Tests**.

## What to submit for evaluation

- Root-cause explanation
- Changed lines only
- Final test output
- Time taken
