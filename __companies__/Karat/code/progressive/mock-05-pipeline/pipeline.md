# Karat Build Pipeline Practice Interview

## Format

- Duration: 50 minutes
- Language: Python
- Target: IC3–IC4
- Structure: one existing codebase for all stages
- Part 1: orient and debug an existing state bug
- Part 2: group completed build durations by worker
- Part 3: calculate peak concurrent builds

## Interviewer rules

- Give one prompt at a time.
- Do not reveal later requirements early.
- Let the candidate run the code and think aloud.
- Ask for an approach before substantial coding.
- Answer only clarifications relevant to the current stage.
- If the candidate is stuck for 2–3 minutes, give only the smallest listed hint.
- Evaluate correctness, communication, tests, complexity, and use of existing abstractions.

## Candidate-visible initial code

```python
import unittest
from io import StringIO


class BuildEvent:
    VALID_EVENT_TYPES = {"START", "FINISH", "CANCEL"}

    def __init__(self, line):
        tokens = line.split()

        if len(tokens) != 4:
            raise ValueError("Expected: timestamp build_id worker_id event_type")

        self.timestamp = int(tokens[0])
        self.build_id = tokens[1]
        self.worker_id = tokens[2]
        self.event_type = tokens[3]

        if self.event_type not in self.VALID_EVENT_TYPES:
            raise ValueError("Invalid event type")


class BuildRun:
    def __init__(self, build_id, worker_id):
        self.build_id = build_id
        self.worker_id = worker_id
        self.started_at = None
        self.finished_at = None

    def record(self, event):
        if event.build_id != self.build_id:
            raise ValueError("Event belongs to a different build")

        if event.worker_id != self.worker_id:
            raise ValueError("Event belongs to a different worker")

        if event.event_type == "START":
            self.started_at = event.timestamp
        elif event.event_type == "FINISH":
            self.finished_at = event.timestamp

    def duration(self):
        if not self.started_at or not self.finished_at:
            return None

        return self.finished_at - self.started_at


class BuildLog:
    def __init__(self, reader):
        self.events = []

        for line in reader:
            line = line.strip()

            if line:
                self.events.append(BuildEvent(line))

    def completed_durations_by_worker(self):
        pass

    def peak_concurrent_builds(self):
        pass


SMALL_LOG = """\
0 build-1 worker-a START
2 build-2 worker-b START
3 build-1 worker-a FINISH
4 build-3 worker-a START
5 build-2 worker-x FINISH
6 build-4 worker-c START
7 build-2 worker-b CANCEL
9 build-3 worker-a FINISH
10 build-4 worker-c FINISH
12 build-1 worker-a START
15 build-1 worker-a FINISH
16 ghost worker-d FINISH
"""


class TestBuildPipeline(unittest.TestCase):
    def test_build_event(self):
        event = BuildEvent("14 build-21 worker-c FINISH")

        self.assertEqual(14, event.timestamp)
        self.assertEqual("build-21", event.build_id)
        self.assertEqual("worker-c", event.worker_id)
        self.assertEqual("FINISH", event.event_type)

    def test_build_run(self):
        run = BuildRun("build-1", "worker-a")
        run.record(BuildEvent("0 build-1 worker-a START"))
        run.record(BuildEvent("9 build-1 worker-a FINISH"))

        self.assertEqual(9, run.duration())

    def test_build_log_loads_events(self):
        log = BuildLog(StringIO(SMALL_LOG))
        self.assertEqual(12, len(log.events))

    def test_completed_durations_by_worker(self):
        log = BuildLog(StringIO(SMALL_LOG))
        log.completed_durations_by_worker();
        self.assertEqual(
            {
                "worker-a": [3, 5, 3],
                "worker-c": [4],
            },
            log.completed_durations_by_worker(),
        )
        
    def test_peak_concurrent_builds(self):
        log = BuildLog(StringIO(SMALL_LOG))
        self.assertEqual(3, log.peak_concurrent_builds())
        

if __name__ == "__main__":
    unittest.main()
```

## Incremental interview script

### 0:00–4:00 — Codebase orientation

**Interviewer instruction**

> This program analyzes events from workers running CI builds. Read the code and explain the responsibilities of `BuildEvent`, `BuildRun`, and `BuildLog`. Then describe how one log line moves through the program.

**Expected interviewee response**

- `BuildEvent` parses and validates one raw line.
- A line contains a timestamp, build ID, worker ID, and event type.
- `BuildRun` stores the lifecycle of one build on one worker.
- `record()` rejects events belonging to another build or worker.
- `duration()` should return elapsed time only after both start and finish exist.
- `BuildLog` loads all nonempty lines and will calculate log-level statistics.
- `StringIO` makes the sample string act like a readable file.

**Evaluation**

- Navigates unfamiliar code quickly.
- Identifies parsing, state, and aggregation responsibilities.
- Notices that timestamps can validly begin at `0`.

### 4:00–10:00 — Run and debug

**Interviewer instruction**

> Run the tests. Diagnose the failure and make the smallest safe fix.

**Expected investigation**

1. Run the file and locate the failing `test_build_run` assertion.
2. Inspect `started_at` and `finished_at` after both events are recorded.
3. Notice that `started_at` equals `0`.
4. Explain that Python treats `0` as false even though it is a valid timestamp.

**Expected fix**

```python
def duration(self):
    if self.started_at is None or self.finished_at is None:
        return None

    return self.finished_at - self.started_at
```

**Small hint if needed**

> Print or inspect both stored timestamps. Are they missing, or merely falsey?

### 10:00–13:00 — Debugging follow-up

**Interviewer instruction**

> Why is `is None` safer here than a truthiness check? Would `if self.started_at == None` work?

**Expected interviewee response**

- `None` means missing; `0` is a real timestamp.
- A truthiness check incorrectly combines those two meanings.
- `== None` often works for built-in values, but `is None` is the standard identity check and cannot be affected by custom equality behavior.

### 13:00–16:00 — Reveal `completed_durations_by_worker`

**Interviewer instruction**

> Implement `completed_durations_by_worker()`.
>
> Return a dictionary mapping each worker ID to a list of durations for builds that worker completed. Preserve completion order within each worker's list.

Do not reveal the detailed lifecycle rules until the candidate asks.

### 16:00–21:00 — Clarify and design

**Expected interviewee questions**

- Are events already in chronological order?
- What should happen to `FINISH` or `CANCEL` without an active `START`?
- Must the worker on `FINISH` or `CANCEL` match the worker on `START`?
- What happens if the same active build receives another `START`?
- Can a build ID be reused after it finishes or is cancelled?
- Should workers with no completed builds appear in the result?

**Interviewer answers**

- Yes, events are already ordered by timestamp.
- Ignore unmatched `FINISH` and `CANCEL` events.
- Yes, the worker must match.
- Ignore a duplicate `START` while that build is active.
- Yes, a build ID may start a new lifecycle after the previous lifecycle ends.
- No, include only workers with at least one completed build.

**Expected design**

> I will scan once and keep an `active_runs` dictionary keyed by build ID. A valid `START` creates a `BuildRun`. A matching `FINISH` records the finish, appends its duration under the worker, and removes the active run. A matching `CANCEL` only removes it. Invalid transitions are ignored.

**Expected complexity**

- Time: `O(n)`, where `n` is the number of events.
- Extra working space: `O(a + c)`, where `a` is the maximum active builds and `c` is the number of completed builds stored in the output.

### 21:00–31:00 — Implement the feature

**Interviewer instruction**

> Implement that approach. Keep explaining the important state changes while coding.

**Expected implementation**

```python
def completed_durations_by_worker(self):
    active_runs = {}
    durations = {}

    for event in self.events:
        run = active_runs.get(event.build_id)

        if event.event_type == "START":
            if run is None:
                run = BuildRun(event.build_id, event.worker_id)
                run.record(event)
                active_runs[event.build_id] = run

        elif event.event_type == "FINISH":
            if run is not None and run.worker_id == event.worker_id:
                run.record(event)
                durations.setdefault(run.worker_id, []).append(run.duration())
                del active_runs[event.build_id]

        elif event.event_type == "CANCEL":
            if run is not None and run.worker_id == event.worker_id:
                del active_runs[event.build_id]

    return durations
```

**What a strong candidate explains**

- The build ID gives constant-time access to active state.
- The active `BuildRun` owns the original worker and start time.
- Removing terminal builds allows the same ID to be reused later.
- A wrong-worker finish does not destroy the valid active run.
- `setdefault()` creates a worker's output list only when needed.

### 31:00–35:00 — Add tests

**Interviewer instruction**

> Add a focused test for the feature, run it, and explain the expected output.

**Expected test**

```python
def test_completed_durations_by_worker(self):
    log = BuildLog(StringIO(SMALL_LOG))

    self.assertEqual(
        {
            "worker-a": [3, 5, 3],
            "worker-c": [4],
        },
        log.completed_durations_by_worker(),
    )
```

**Expected reasoning**

- `build-1` first runs from `0` to `3`, taking `3`.
- `build-3` runs from `4` to `9`, taking `5`.
- The wrong-worker finish for `build-2` is ignored; its matching cancel removes it.
- `build-4` takes `4`.
- Reused `build-1` takes another `3`.
- The unmatched `ghost` finish is ignored.

### 35:00–38:00 — Reveal `peak_concurrent_builds`

**Interviewer instruction**

> Implement `peak_concurrent_builds()`. Return the largest number of builds active at the same time. Use the same lifecycle rules as the previous feature.

### 38:00–44:00 — Design and implement peak concurrency

**Expected design**

> I only need active build IDs and their workers. On a new valid `START`, add the build and update the maximum. On a matching `FINISH` or `CANCEL`, remove it. Duplicate starts and invalid terminal events do not change the count.

**Expected implementation**

```python
def peak_concurrent_builds(self):
    active_workers = {}
    peak = 0

    for event in self.events:
        active_worker = active_workers.get(event.build_id)

        if event.event_type == "START":
            if active_worker is None:
                active_workers[event.build_id] = event.worker_id
                peak = max(peak, len(active_workers))

        elif event.event_type in {"FINISH", "CANCEL"}:
            if active_worker == event.worker_id:
                del active_workers[event.build_id]

    return peak
```

**Expected test**

```python
def test_peak_concurrent_builds(self):
    log = BuildLog(StringIO(SMALL_LOG))
    self.assertEqual(3, log.peak_concurrent_builds())
```

**Expected reasoning**

- At timestamp `6`, `build-2`, `build-3`, and `build-4` are all active.
- Therefore, the peak is `3`.

### 44:00–47:00 — Edge cases

**Interviewer instruction**

> Which additional edge cases would you test?

**Expected interviewee response**

- Empty input returns `{}` and peak `0`.
- Only unmatched terminal events produce no durations and peak `0`.
- A duplicate active `START` does not reset its start time or increase concurrency.
- A wrong-worker finish or cancel does not close the active build.
- A matching cancel closes a build but adds no duration.
- A build ID can be reused after finish or cancel.
- Several builds may run on the same worker and still count separately.
- Timestamp `0` remains valid.

**Optional hidden test**

```python
def test_duplicate_start_does_not_reset_run(self):
    data = """\
0 build-1 worker-a START
4 build-1 worker-a START
9 build-1 worker-a FINISH
"""
    log = BuildLog(StringIO(data))

    self.assertEqual(
        {"worker-a": [9]},
        log.completed_durations_by_worker(),
    )
    self.assertEqual(1, log.peak_concurrent_builds())
```

### 47:00–50:00 — Complexity and unordered input

**Interviewer instruction**

> State the complexity of both features. What changes if events are not ordered by timestamp?

**Expected interviewee response**

- Each current feature scans `n` events once: `O(n)` time.
- Active state uses `O(a)` space, where `a` is maximum concurrent builds.
- The duration method additionally returns `O(c)` duration values.
- For unordered input, sort events by timestamp first: `O(n log n)` time, followed by the same scan.
- If equal timestamps are possible, the product must define a tie-breaking rule, such as processing terminal events before starts or preserving input order.

## Optional IC4 follow-ups

Ask only if time remains.

### Follow-up A — Avoid duplicated lifecycle logic

> Both methods implement similar event transitions. How would you reduce duplication?

**Expected response**

- Create one iterator or state-machine helper that emits lifecycle changes such as `started`, `completed`, and `cancelled`.
- Both aggregations can consume those transitions.
- Keep aggregation rules separate from validation/state-transition rules.
- Avoid forcing an abstraction until the repeated rules are stable and well tested.

### Follow-up B — Very large log files

> How would you process a file that does not fit in memory?

**Expected response**

- Process the reader line by line rather than storing all events.
- Maintain only active build state and required aggregates.
- This preserves `O(a + c)` memory for durations, or `O(a)` if durations are streamed to another sink.
- If the input is unordered, external sorting or upstream ordering is required.

### Follow-up C — Same build starts on another worker

> Product now says a second `START` for an active build means the build was reassigned. What must change?

**Expected response**

- Clarify whether reassignment cancels the first attempt or continues its original start time.
- Encode that rule in one state-transition function.
- Update both duration and peak calculations consistently.
- Add a test before changing the implementation.

## Common mistakes

- Treating timestamp `0` as missing.
- Overwriting an active run on a duplicate `START` and losing its real start time.
- Closing a build on a wrong-worker `FINISH` or `CANCEL`.
- Keeping finished or cancelled builds active.
- Counting a cancelled build as completed.
- Preventing valid build-ID reuse after a terminal event.
- Counting workers instead of builds for peak concurrency.
- Sorting unnecessarily when the ordering guarantee was already clarified.
- Giving complexity without defining variables.

## Scoring guide

| Area | Strong signal |
| --- | --- |
| Orientation | Explains parsing, object state, and aggregation clearly |
| Debugging | Reproduces the failure and distinguishes missing from falsey |
| Clarification | Confirms ordering, matching workers, duplicates, cancellation, and ID reuse |
| Data structures | Uses a build-keyed dictionary for active state |
| Correctness | Handles invalid transitions without corrupting valid state |
| Reuse | Uses `BuildRun` where it adds value and avoids duplicated duration rules |
| Testing | Covers timestamp zero, duplicates, wrong workers, cancellation, and reuse |
| Complexity | States `O(n)` time and defines active/output space |
| Communication | Explains the state machine before and during implementation |

## Interviewer stopping rule

End when the candidate has:

1. Fixed the timestamp-zero bug.
2. Implemented and tested `completed_durations_by_worker()`.
3. Implemented and tested `peak_concurrent_builds()`.
4. Explained at least three edge cases.
5. Stated correct time and space complexity.

