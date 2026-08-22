# OnePay Karat Practice Interview

## Format

- Duration: about 40 minutes
- Language: Python
- Structure: one existing codebase used for both parts
- Part 1: codebase orientation and debugging
- Part 2: progressive implementation and testing

## Rules for the interviewer

- Give only one prompt at a time.
- Do not reveal the bug or implementation before the candidate investigates.
- Let the candidate think aloud.
- Answer clarification questions only with information from the current stage.
- If the candidate is stuck for 2–3 minutes, give the smallest hint listed.
- Evaluate correctness, communication, readability, tests, and complexity.

## Initial code given to the candidate

```python
import unittest
from io import StringIO


class LogEntry:
    def __init__(self, log_line):
        tokens = log_line.split()

        self.timestamp = tokens[0]
        self.license_plate = tokens[1]
        self.booth_type = tokens[3]

        location_direction = tokens[2]
        self.location = int(location_direction[:-1])

        direction = location_direction[-1]

        if direction == "E":
            self.direction = "EAST"
        elif direction == "W":
            self.direction = "WEST"
        else:
            raise ValueError("Invalid direction")


class LogFile:
    def __init__(self, reader):
        self.log_entries = []

        for line in reader:
            line = line.strip()

            if line:
                self.log_entries.append(LogEntry(line))

    def count_journeys(self):
        pass

    def get(self, index):
        return self.log_entries[index]

    def size(self):
        return len(self.log_entries)


SMALL_LOG = """\
90750.191 JOX304 250E ENTRY
91081.684 JOX304 260E MAINROAD
91082.101 THX138 110E ENTRY
91483.251 JOX304 270E MAINROAD
91873.920 THX138 120E MAINROAD
91874.493 JOX304 280E EXIT
91982.102 THX138 290E EXIT
92301.302 THX138 300E ENTRY
92371.302 THX138 310E EXIT
92400.000 BAD111 320E ENTRY
92500.000 BAD222 330E EXIT
92600.000 JOX304 340E MAINROAD
92700.000 ABC123 350W MAINROAD
"""


class TestTollBooth(unittest.TestCase):
    def test_log_file(self):
        log_file = LogFile(StringIO(SMALL_LOG))

        self.assertEqual(13, log_file.size())
        self.assertTrue(
            all(
                isinstance(entry, LogEntry)
                for entry in log_file.log_entries
            )
        )

    def test_log_entry(self):
        entry = LogEntry("44776.619 KTB918 310E MAINROAD")

        self.assertAlmostEqual(44776.619, entry.timestamp, places=3)
        self.assertEqual("KTB918", entry.license_plate)
        self.assertEqual(310, entry.location)
        self.assertEqual("EAST", entry.direction)
        self.assertEqual("MAINROAD", entry.booth_type)

        entry = LogEntry("52160.132 ABC123 400W ENTRY")

        self.assertAlmostEqual(52160.132, entry.timestamp, places=3)
        self.assertEqual("WEST", entry.direction)
        self.assertEqual("ENTRY", entry.booth_type)

    def test_count_journeys(self):
        log_file = LogFile(StringIO(SMALL_LOG))
        self.assertEqual(3, log_file.count_journeys())


if __name__ == "__main__":
    unittest.main()
```

## Incremental interview script

### 0:00–3:00 — Introduction and orientation

**Interviewer instruction**

> You are given a small program that analyzes highway tollbooth logs. Please read the code, explain what each class does, and describe how one raw log line is processed. Think aloud.

**Expected interviewee response**

- `LogEntry` parses one line into timestamp, plate, booth type, location, and direction.
- `LogFile` reads lines and stores `LogEntry` objects.
- `StringIO` makes the string test data behave like a file.
- `TestTollBooth` verifies parsing, file loading, and journey counting.
- `unittest.main()` discovers and runs methods beginning with `test_`.

**Evaluation**

- Candidate can navigate unfamiliar code.
- Candidate identifies the input format and important fields.
- Candidate communicates before editing.

### 3:00–10:00 — Run and debug the existing tests

**Interviewer instruction**

> Please run the tests, diagnose the current failure, and make the smallest safe fix.

**Expected interviewee response**

1. Run the file and inspect the failing assertion or exception.
2. Notice that `timestamp` is stored as a string.
3. Explain that `assertAlmostEqual()` expects numeric values.
4. Change:

```python
self.timestamp = tokens[0]
```

to:

```python
self.timestamp = float(tokens[0])
```

5. Run the tests again and explain that the parsing tests now pass while `count_journeys()` remains unimplemented.

**Small hint if needed**

> Compare the runtime type of each parsed field with what its test expects.

### 10:00–14:00 — Explain the fix

**Interviewer instruction**

> Why is converting the timestamp during parsing better than converting it inside each test or consumer?

**Expected interviewee response**

- A `LogEntry` should maintain a consistent data model.
- Every consumer receives a numeric timestamp.
- Numeric timestamps support correct comparison and arithmetic.
- Parsing and validation belong at the input boundary.

### 14:00–17:00 — Reveal Part 2

**Interviewer instruction**

> Implement `count_journeys()` so it returns the total number of complete journeys.
>
> A complete journey consists of the same vehicle passing an `ENTRY`, then zero or more `MAINROAD` booths, and then an `EXIT` in log order.

Do not reveal more rules unless the candidate asks.

### 17:00–21:00 — Clarification and design

**Expected interviewee questions**

- Are log entries already ordered by increasing timestamp?
- Can a journey contain zero `MAINROAD` records?
- Should `ENTRY` and `EXIT` have the same direction?
- What should happen to an `EXIT` without an earlier `ENTRY`?
- What should happen if the same plate has another `ENTRY` before exiting?

**Interviewer answers for this practice**

- Yes, entries are already ordered by timestamp.
- Yes, `ENTRY → EXIT` is complete.
- Yes, the direction must match.
- Ignore an unmatched `EXIT`.
- A later `ENTRY` replaces the earlier active entry for that plate.

**Expected interviewee design**

> I will scan the logs once and keep a dictionary from license plate to its active direction. On `ENTRY`, I store or replace the direction. I can ignore `MAINROAD`. On a matching `EXIT`, I increase the count and remove the plate. This takes O(n) time and O(v) space, where v is the number of active vehicles.

**Evaluation**

- Candidate clarifies ambiguity instead of guessing silently.
- Candidate recognizes that `MAINROAD` does not affect the count.
- Candidate chooses a dictionary for constant-time state lookup.

### 21:00–31:00 — Implementation

**Interviewer instruction**

> Please implement your approach. Keep explaining the important decisions while coding.

**Expected interviewee implementation**

```python
def count_journeys(self):
    active_directions = {}
    journey_count = 0

    for entry in self.log_entries:
        plate = entry.license_plate

        if entry.booth_type == "ENTRY":
            active_directions[plate] = entry.direction

        elif entry.booth_type == "EXIT":
            if active_directions.get(plate) == entry.direction:
                journey_count += 1
                del active_directions[plate]

    return journey_count
```

**What a strong candidate explains**

- `MAINROAD` falls through and is ignored.
- `.get(plate)` safely handles a missing plate.
- Deleting a completed vehicle prevents two exits from counting twice.
- A new `ENTRY` naturally replaces stale state for the same plate.

### 31:00–36:00 — Test and expose hidden cases

**Interviewer instruction**

> Run the tests. Then tell me which additional edge cases you would add.

**Expected interviewee response**

- Empty log returns `0`.
- Only `ENTRY` returns `0`.
- One or repeated unmatched `EXIT` records return `0`.
- `ENTRY → EXIT` with no `MAINROAD` returns `1`.
- `ENTRY → MAINROAD → EXIT` returns `1`.
- Multiple completed journeys for one plate are all counted.
- Interleaved logs from several plates are handled independently.
- Opposite-direction `EXIT` does not complete the journey.
- A second `ENTRY` replaces the earlier active direction.

**Optional hidden test**

```python
def test_unmatched_repeated_exits(self):
    data = """\
1.000 BAD222 330E EXIT
2.000 BAD222 340E EXIT
"""
    self.assertEqual(0, LogFile(StringIO(data)).count_journeys())
```

### 36:00–40:00 — Complexity and follow-up

**Interviewer instruction**

> What are the time and space complexities? How would your solution change if the logs were not ordered?

**Expected interviewee response**

- Current solution: `O(n)` time and `O(v)` space.
- If logs are unordered: sort by timestamp first, producing `O(n log n)` time, then use the same scan.
- The scan still requires `O(v)` active state; sorting may require additional memory depending on the sorting implementation.

## Common mistakes the interviewer should watch for

- Counting total entries and exits without respecting their order.
- Counting repeated exits after only one entry.
- Requiring at least one `MAINROAD` event.
- Treating an unmatched exit as an active journey.
- Leaving completed plates in active state with an empty-string sentinel.
- Comparing timestamps as strings.
- Using `==` incorrectly in another language where string value comparison differs.
- Giving complexity without defining variables.
- Writing code silently without explaining the approach.

## Final scoring guide

| Area | Strong signal |
| --- | --- |
| Orientation | Explains the code flow accurately and quickly |
| Debugging | Reproduces the failure and makes the smallest correct fix |
| Clarification | Confirms ordering, zero `MAINROAD`, direction, and invalid sequences |
| Data structure | Uses a plate-to-active-direction dictionary |
| Correctness | Counts only ordered, matching, complete journeys |
| Code quality | Uses clear names, removes completed state, avoids debug prints |
| Testing | Covers incomplete, repeated, interleaved, and direction cases |
| Complexity | Correctly states `O(n)` time and `O(v)` space |

## Interviewer stopping rule

End the exercise when the candidate has:

1. Fixed timestamp parsing.
2. Implemented journey counting.
3. Passed the supplied tests.
4. Explained at least three edge cases.
5. Given correct time and space complexity.

