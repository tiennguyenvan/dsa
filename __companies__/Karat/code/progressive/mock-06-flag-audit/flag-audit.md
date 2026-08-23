# Karat Feature Flag Audit Practice Interview

## Format

- Duration: 50 minutes
- Language: Python
- Target: IC3–IC4
- Structure: one existing codebase for every stage
- Part 1: orient and debug an existing timestamp-state bug
- Part 2: integrate current rollout calculation
- Part 3: integrate rollout exposure calculation

## Interviewer rules

- Give only one prompt at a time.
- Do not reveal later requirements early.
- Let the candidate run the tests and think aloud.
- Ask for an approach before substantial coding.
- Answer only clarifications relevant to the current stage.
- If the candidate is stuck for 2–3 minutes, give the smallest listed hint.
- Evaluate correctness, communication, edge cases, tests, complexity, and reuse of existing abstractions.

---

# Candidate Starter File

Give this code at the beginning. It contains the complete debugging test suite. Add the integration tests only when their stage is revealed.

```python
import unittest
from io import StringIO


class FlagEvent:
    VALID_ACTIONS = {"SET", "DELETE"}

    def __init__(self, line):
        tokens = line.split()

        if len(tokens) != 5:
            raise ValueError(
                "Expected: timestamp service flag action rollout"
            )

        self.timestamp = int(tokens[0])
        self.service = tokens[1]
        self.flag = tokens[2]
        self.action = tokens[3]

        if self.action not in self.VALID_ACTIONS:
            raise ValueError("Invalid action")

        if self.action == "SET":
            self.rollout = int(tokens[4])

            if not 0 <= self.rollout <= 100:
                raise ValueError("Rollout must be between 0 and 100")
        else:
            if tokens[4] != "-":
                raise ValueError("DELETE rollout must be -")

            self.rollout = 0


class FeatureFlag:
    def __init__(self, service, flag):
        self.service = service
        self.flag = flag
        self.rollout = 0
        self.updated_at = None

    def apply(self, event):
        if event.service != self.service or event.flag != self.flag:
            raise ValueError("Event belongs to a different feature flag")

        # There is an intentional bug in this condition.
        if not self.updated_at or event.timestamp >= self.updated_at:
            self.rollout = event.rollout
            self.updated_at = event.timestamp


class AuditLog:
    def __init__(self, reader):
        self.events = []

        for line in reader:
            line = line.strip()

            if line:
                self.events.append(FlagEvent(line))

    def current_rollouts(self):
        pass

    def rollout_exposure_by_service(self, end_time):
        pass


class TestDebugFeatureFlag(unittest.TestCase):
    def test_parses_set_event(self):
        event = FlagEvent("12 billing new-checkout SET 40")

        self.assertEqual(12, event.timestamp)
        self.assertEqual("billing", event.service)
        self.assertEqual("new-checkout", event.flag)
        self.assertEqual("SET", event.action)
        self.assertEqual(40, event.rollout)

    def test_parses_delete_event(self):
        event = FlagEvent("15 billing new-checkout DELETE -")

        self.assertEqual("DELETE", event.action)
        self.assertEqual(0, event.rollout)

    def test_rejects_invalid_action(self):
        with self.assertRaises(ValueError):
            FlagEvent("1 billing new-checkout ENABLE 20")

    def test_rejects_invalid_rollout(self):
        with self.assertRaises(ValueError):
            FlagEvent("1 billing new-checkout SET 101")

        with self.assertRaises(ValueError):
            FlagEvent("1 billing new-checkout SET -1")

    def test_rejects_delete_with_numeric_rollout(self):
        with self.assertRaises(ValueError):
            FlagEvent("1 billing new-checkout DELETE 0")

    def test_rejects_event_for_different_flag(self):
        state = FeatureFlag("billing", "new-checkout")

        with self.assertRaises(ValueError):
            state.apply(FlagEvent("1 billing other-flag SET 10"))

    def test_applies_newer_event(self):
        state = FeatureFlag("billing", "new-checkout")
        state.apply(FlagEvent("3 billing new-checkout SET 20"))
        state.apply(FlagEvent("8 billing new-checkout SET 60"))

        self.assertEqual(60, state.rollout)
        self.assertEqual(8, state.updated_at)

    def test_same_timestamp_uses_later_log_event(self):
        state = FeatureFlag("billing", "new-checkout")
        state.apply(FlagEvent("3 billing new-checkout SET 20"))
        state.apply(FlagEvent("3 billing new-checkout SET 60"))

        self.assertEqual(60, state.rollout)

    def test_ignores_older_event_after_timestamp_zero(self):
        state = FeatureFlag("billing", "new-checkout")
        state.apply(FlagEvent("0 billing new-checkout SET 25"))
        state.apply(FlagEvent("-1 billing new-checkout SET 90"))

        self.assertEqual(25, state.rollout)
        self.assertEqual(0, state.updated_at)


if __name__ == "__main__":
    unittest.main()
```

---

# Incremental Interview Script

## 0:00–4:00 — Codebase orientation

**Interviewer instruction**

> This program processes audit events for feature-flag rollouts. Read the code and explain the responsibilities of `FlagEvent`, `FeatureFlag`, and `AuditLog`. Then describe how one raw line moves through the program.

**Expected interviewee response**

- `FlagEvent` parses and validates one audit line.
- `SET` carries a rollout percentage from `0` through `100`.
- `DELETE` uses `-` in the input and becomes rollout `0` internally.
- `FeatureFlag` stores the latest state for one `(service, flag)` pair.
- `FeatureFlag.apply()` rejects events for another flag and ignores older updates.
- When timestamps tie, the later event in log order wins.
- `AuditLog` loads all events and will provide cross-flag aggregations.

## 4:00–11:00 — Debug the existing state bug

**Interviewer instruction**

> Run the debugging tests. Diagnose the failure and make the smallest safe fix. Do not implement the `AuditLog` methods yet.

**Expected investigation**

1. Run the tests.
2. Observe that `test_ignores_older_event_after_timestamp_zero` fails.
3. Notice that `updated_at == 0` is a valid timestamp but is falsey.
4. A stale event at timestamp `-1` is therefore incorrectly accepted.

**Expected fix**

```python
if self.updated_at is None or event.timestamp >= self.updated_at:
```

**Expected explanation**

- `None` means no event has been applied.
- `0` is valid data, not missing state.
- An explicit identity check separates those cases.
- `>=` intentionally makes a later log event win when timestamps tie.

**Small hint if needed**

> Is timestamp `0` missing, or is it a valid value that happens to be falsey?

## 11:00–14:00 — Debugging follow-up

**Interviewer instruction**

> Why not change the condition to only `event.timestamp >= self.updated_at`?

**Expected response**

- Before the first event, `updated_at` is `None`.
- Comparing an integer with `None` raises `TypeError` in Python 3.
- The explicit `None` branch safely handles the initial state.

---

## 14:00–17:00 — Reveal integration Part 1

**Interviewer instruction**

> Implement `current_rollouts()`.
>
> Return a nested dictionary in this shape:
>
> ```python
> {
>     "service": {
>         "flag": rollout_percentage,
>     }
> }
> ```
>
> Only flags whose latest rollout is greater than zero should appear.

Do not reveal Part 2 yet.

## 17:00–20:00 — Clarify and design Part 1

**Expected interviewee questions and answers**

| Question | Interviewer answer |
| --- | --- |
| Are events ordered? | No. Events may be out of timestamp order. |
| What if timestamps tie? | The event appearing later in the log wins. |
| What does `DELETE` do? | It makes the flag inactive with rollout `0`. |
| Can a later `SET` reactivate a deleted flag? | Yes. |
| Should `SET 0` appear? | No. Only rollouts greater than zero appear. |
| Can different services use the same flag name? | Yes. Treat them independently. |

**Expected design**

> I will use a dictionary keyed by `(service, flag)`. Each value will be a `FeatureFlag`. I will apply every event through the existing `apply()` method, then build the nested result from states whose rollout is greater than zero.

**Expected complexity**

- Time: `O(n)` for `n` events.
- Space: `O(f + o)`, where `f` is the number of distinct flags and `o` is the output size.

## 20:00–28:00 — Add all Part 1 tests and implement

Add this complete test class to the candidate file:

```python
class TestCurrentRollouts(unittest.TestCase):
    def make_log(self, data):
        return AuditLog(StringIO(data))

    def test_empty_log(self):
        self.assertEqual({}, self.make_log("").current_rollouts())

    def test_groups_active_flags_by_service(self):
        log = self.make_log("""\
1 billing new-checkout SET 25
2 billing invoice-search SET 70
3 identity passkeys SET 10
""")

        self.assertEqual(
            {
                "billing": {
                    "new-checkout": 25,
                    "invoice-search": 70,
                },
                "identity": {"passkeys": 10},
            },
            log.current_rollouts(),
        )

    def test_uses_latest_timestamp_when_out_of_order(self):
        log = self.make_log("""\
10 billing new-checkout SET 80
3 billing new-checkout SET 20
7 billing new-checkout SET 50
""")

        self.assertEqual(
            {"billing": {"new-checkout": 80}},
            log.current_rollouts(),
        )

    def test_same_timestamp_uses_later_log_event(self):
        log = self.make_log("""\
5 billing new-checkout SET 20
5 billing new-checkout SET 65
""")

        self.assertEqual(
            {"billing": {"new-checkout": 65}},
            log.current_rollouts(),
        )

    def test_delete_removes_flag(self):
        log = self.make_log("""\
1 billing new-checkout SET 25
2 billing invoice-search SET 70
3 billing new-checkout DELETE -
""")

        self.assertEqual(
            {"billing": {"invoice-search": 70}},
            log.current_rollouts(),
        )

    def test_newer_set_reactivates_deleted_flag(self):
        log = self.make_log("""\
1 billing new-checkout SET 25
5 billing new-checkout DELETE -
9 billing new-checkout SET 40
""")

        self.assertEqual(
            {"billing": {"new-checkout": 40}},
            log.current_rollouts(),
        )

    def test_older_set_does_not_reactivate_deleted_flag(self):
        log = self.make_log("""\
5 billing new-checkout DELETE -
2 billing new-checkout SET 90
""")

        self.assertEqual({}, log.current_rollouts())

    def test_set_zero_is_omitted(self):
        log = self.make_log("""\
1 billing new-checkout SET 0
2 identity passkeys SET 10
""")

        self.assertEqual(
            {"identity": {"passkeys": 10}},
            log.current_rollouts(),
        )

    def test_same_flag_name_in_different_services_is_independent(self):
        log = self.make_log("""\
1 billing redesign SET 20
2 identity redesign SET 80
3 billing redesign DELETE -
""")

        self.assertEqual(
            {"identity": {"redesign": 80}},
            log.current_rollouts(),
        )
```

**Expected implementation**

```python
def current_rollouts(self):
    states = {}

    for event in self.events:
        key = (event.service, event.flag)

        if key not in states:
            states[key] = FeatureFlag(event.service, event.flag)

        states[key].apply(event)

    result = {}

    for state in states.values():
        if state.rollout <= 0:
            continue

        result.setdefault(state.service, {})[state.flag] = state.rollout

    return result
```

**Strong candidate explanation**

- The composite key prevents collisions between services.
- Reusing `FeatureFlag.apply()` keeps timestamp conflict rules in one place.
- Deleted and zero-rollout flags are excluded during result construction.
- An empty service dictionary is never created.

---

## 28:00–31:00 — Reveal integration Part 2

**Interviewer instruction**

> Implement `rollout_exposure_by_service(end_time)`.
>
> Exposure is `rollout percentage × seconds active`. Sum the exposure of every flag belonging to the same service from its first event through `end_time`.
>
> Example: a flag is set to `20` at time `2`, changed to `50` at time `5`, and deleted at time `7`. With `end_time = 10`, its exposure is:
>
> ```text
> 20 × (5 - 2) + 50 × (7 - 5) = 160
> ```

## 31:00–34:00 — Clarify and design Part 2

**Expected interviewee questions and answers**

| Question | Interviewer answer |
| --- | --- |
| Are events ordered? | No. Process each flag in timestamp order. |
| What if timestamps tie? | Preserve log order; the later log event wins from that instant onward. |
| What is exposure before a flag's first event? | Zero. |
| What does `DELETE` contribute? | It changes rollout to zero. |
| What about events after `end_time`? | Ignore them. |
| Should services with zero total exposure appear? | No. |
| Do flags overlap? | Yes. Sum each flag's exposure into its service total. |

**Expected design**

> I will group events by `(service, flag)` while retaining their original indexes. For each flag, I will stable-sort by timestamp, accumulate the previous rollout over each time interval, apply the next rollout, and finally accumulate through `end_time`. Then I will add positive flag exposure to its service.

**Expected complexity**

- Grouping: `O(n)` time and `O(n)` space.
- Sorting: `O(n log n)` worst case across all groups.
- Scanning: `O(n)` time.
- Total: `O(n log n)` time and `O(n + s)` space, where `s` is the number of services in the result.

## 34:00–44:00 — Add all Part 2 tests and implement

Add this complete test class:

```python
class TestRolloutExposure(unittest.TestCase):
    def make_log(self, data):
        return AuditLog(StringIO(data))

    def test_empty_log(self):
        self.assertEqual(
            {},
            self.make_log("").rollout_exposure_by_service(10),
        )

    def test_single_set_runs_until_end_time(self):
        log = self.make_log("2 billing new-checkout SET 25\n")

        self.assertEqual(
            {"billing": 200},
            log.rollout_exposure_by_service(10),
        )

    def test_set_change_and_delete(self):
        log = self.make_log("""\
2 billing new-checkout SET 20
5 billing new-checkout SET 50
7 billing new-checkout DELETE -
""")

        self.assertEqual(
            {"billing": 160},
            log.rollout_exposure_by_service(10),
        )

    def test_out_of_order_events_are_processed_chronologically(self):
        log = self.make_log("""\
7 billing new-checkout DELETE -
2 billing new-checkout SET 20
5 billing new-checkout SET 50
""")

        self.assertEqual(
            {"billing": 160},
            log.rollout_exposure_by_service(10),
        )

    def test_same_timestamp_uses_later_log_event(self):
        log = self.make_log("""\
2 billing new-checkout SET 20
2 billing new-checkout SET 60
""")

        self.assertEqual(
            {"billing": 180},
            log.rollout_exposure_by_service(5),
        )

    def test_multiple_flags_in_one_service_are_summed(self):
        log = self.make_log("""\
0 billing new-checkout SET 20
2 billing invoice-search SET 50
4 billing new-checkout DELETE -
""")

        # new-checkout: 20 * 4 = 80
        # invoice-search: 50 * 4 = 200
        self.assertEqual(
            {"billing": 280},
            log.rollout_exposure_by_service(6),
        )

    def test_services_are_independent(self):
        log = self.make_log("""\
0 billing redesign SET 20
1 identity redesign SET 50
""")

        self.assertEqual(
            {
                "billing": 100,
                "identity": 200,
            },
            log.rollout_exposure_by_service(5),
        )

    def test_events_after_end_time_are_ignored(self):
        log = self.make_log("""\
2 billing new-checkout SET 25
8 billing new-checkout SET 90
9 identity passkeys SET 100
""")

        self.assertEqual(
            {"billing": 75},
            log.rollout_exposure_by_service(5),
        )

    def test_deleted_flag_can_be_reactivated(self):
        log = self.make_log("""\
0 billing new-checkout SET 20
2 billing new-checkout DELETE -
5 billing new-checkout SET 30
""")

        # 20 * 2 + 30 * 3
        self.assertEqual(
            {"billing": 130},
            log.rollout_exposure_by_service(8),
        )

    def test_zero_rollout_and_delete_produce_no_output(self):
        log = self.make_log("""\
0 billing new-checkout SET 0
2 identity passkeys DELETE -
""")

        self.assertEqual(
            {},
            log.rollout_exposure_by_service(8),
        )

    def test_event_exactly_at_end_time_adds_no_exposure(self):
        log = self.make_log("5 billing new-checkout SET 100\n")

        self.assertEqual(
            {},
            log.rollout_exposure_by_service(5),
        )
```

**Expected implementation**

```python
def rollout_exposure_by_service(self, end_time):
    events_by_flag = {}

    for index, event in enumerate(self.events):
        if event.timestamp <= end_time:
            key = (event.service, event.flag)
            events_by_flag.setdefault(key, []).append((index, event))

    result = {}

    for (service, _), indexed_events in events_by_flag.items():
        indexed_events.sort(key=lambda item: (item[1].timestamp, item[0]))

        rollout = 0
        previous_time = indexed_events[0][1].timestamp
        exposure = 0

        for _, event in indexed_events:
            exposure += rollout * (event.timestamp - previous_time)
            rollout = event.rollout
            previous_time = event.timestamp

        exposure += rollout * (end_time - previous_time)

        if exposure > 0:
            result[service] = result.get(service, 0) + exposure

    return result
```

**Strong candidate explanation**

- Including the original index makes the tie rule explicit even if the sort implementation changes.
- The old rollout applies to the interval before the next event.
- A `DELETE` is naturally handled because its parsed rollout is `0`.
- Events at `end_time` have a zero-length interval unless an earlier rollout was already active.
- Exposure is computed separately per flag before being summed by service.

---

## 44:00–48:00 — Run the complete suite and analyze edge cases

**Interviewer instruction**

> Run all tests. Explain which cases protect the most important state and integration rules.

**Expected response**

- Timestamp zero is different from missing state.
- Out-of-order events must not overwrite newer current state.
- Equal timestamps use log order.
- A composite `(service, flag)` key prevents cross-service collisions.
- `DELETE` removes current state and stops future exposure.
- A later `SET` reactivates a deleted flag.
- Multiple flags contribute independently to one service's exposure.
- Future events and zero-length intervals add no exposure.

## 48:00–50:00 — Complexity and follow-up

**Interviewer instruction**

> State the time and space complexity of both methods. What changes if the system guarantees that the log is already ordered by timestamp?

**Expected response**

- `current_rollouts()`: `O(n)` time and `O(f + o)` space.
- `rollout_exposure_by_service()`: `O(n log n)` time and `O(n + s)` space because events are grouped and sorted.
- If input is globally chronological, exposure can be accumulated in one scan with per-flag state, reducing it to `O(n)` time and `O(f + s)` space.
- The one-pass version still needs a final scan to accumulate every active flag from its last update through `end_time`.

---

# Complete Reference Implementation

Use this only after the mock interview or to verify the full test suite.

```python
import unittest
from io import StringIO


class FlagEvent:
    VALID_ACTIONS = {"SET", "DELETE"}

    def __init__(self, line):
        tokens = line.split()

        if len(tokens) != 5:
            raise ValueError(
                "Expected: timestamp service flag action rollout"
            )

        self.timestamp = int(tokens[0])
        self.service = tokens[1]
        self.flag = tokens[2]
        self.action = tokens[3]

        if self.action not in self.VALID_ACTIONS:
            raise ValueError("Invalid action")

        if self.action == "SET":
            self.rollout = int(tokens[4])

            if not 0 <= self.rollout <= 100:
                raise ValueError("Rollout must be between 0 and 100")
        else:
            if tokens[4] != "-":
                raise ValueError("DELETE rollout must be -")

            self.rollout = 0


class FeatureFlag:
    def __init__(self, service, flag):
        self.service = service
        self.flag = flag
        self.rollout = 0
        self.updated_at = None

    def apply(self, event):
        if event.service != self.service or event.flag != self.flag:
            raise ValueError("Event belongs to a different feature flag")

        if self.updated_at is None or event.timestamp >= self.updated_at:
            self.rollout = event.rollout
            self.updated_at = event.timestamp


class AuditLog:
    def __init__(self, reader):
        self.events = []

        for line in reader:
            line = line.strip()

            if line:
                self.events.append(FlagEvent(line))

    def current_rollouts(self):
        states = {}

        for event in self.events:
            key = (event.service, event.flag)

            if key not in states:
                states[key] = FeatureFlag(event.service, event.flag)

            states[key].apply(event)

        result = {}

        for state in states.values():
            if state.rollout <= 0:
                continue

            result.setdefault(state.service, {})[state.flag] = state.rollout

        return result

    def rollout_exposure_by_service(self, end_time):
        events_by_flag = {}

        for index, event in enumerate(self.events):
            if event.timestamp <= end_time:
                key = (event.service, event.flag)
                events_by_flag.setdefault(key, []).append((index, event))

        result = {}

        for (service, _), indexed_events in events_by_flag.items():
            indexed_events.sort(
                key=lambda item: (item[1].timestamp, item[0])
            )

            rollout = 0
            previous_time = indexed_events[0][1].timestamp
            exposure = 0

            for _, event in indexed_events:
                exposure += rollout * (event.timestamp - previous_time)
                rollout = event.rollout
                previous_time = event.timestamp

            exposure += rollout * (end_time - previous_time)

            if exposure > 0:
                result[service] = result.get(service, 0) + exposure

        return result


class TestDebugFeatureFlag(unittest.TestCase):
    def test_parses_set_event(self):
        event = FlagEvent("12 billing new-checkout SET 40")
        self.assertEqual(12, event.timestamp)
        self.assertEqual("billing", event.service)
        self.assertEqual("new-checkout", event.flag)
        self.assertEqual("SET", event.action)
        self.assertEqual(40, event.rollout)

    def test_parses_delete_event(self):
        event = FlagEvent("15 billing new-checkout DELETE -")
        self.assertEqual("DELETE", event.action)
        self.assertEqual(0, event.rollout)

    def test_rejects_invalid_action(self):
        with self.assertRaises(ValueError):
            FlagEvent("1 billing new-checkout ENABLE 20")

    def test_rejects_invalid_rollout(self):
        with self.assertRaises(ValueError):
            FlagEvent("1 billing new-checkout SET 101")
        with self.assertRaises(ValueError):
            FlagEvent("1 billing new-checkout SET -1")

    def test_rejects_delete_with_numeric_rollout(self):
        with self.assertRaises(ValueError):
            FlagEvent("1 billing new-checkout DELETE 0")

    def test_rejects_event_for_different_flag(self):
        state = FeatureFlag("billing", "new-checkout")
        with self.assertRaises(ValueError):
            state.apply(FlagEvent("1 billing other-flag SET 10"))

    def test_applies_newer_event(self):
        state = FeatureFlag("billing", "new-checkout")
        state.apply(FlagEvent("3 billing new-checkout SET 20"))
        state.apply(FlagEvent("8 billing new-checkout SET 60"))
        self.assertEqual(60, state.rollout)
        self.assertEqual(8, state.updated_at)

    def test_same_timestamp_uses_later_log_event(self):
        state = FeatureFlag("billing", "new-checkout")
        state.apply(FlagEvent("3 billing new-checkout SET 20"))
        state.apply(FlagEvent("3 billing new-checkout SET 60"))
        self.assertEqual(60, state.rollout)

    def test_ignores_older_event_after_timestamp_zero(self):
        state = FeatureFlag("billing", "new-checkout")
        state.apply(FlagEvent("0 billing new-checkout SET 25"))
        state.apply(FlagEvent("-1 billing new-checkout SET 90"))
        self.assertEqual(25, state.rollout)
        self.assertEqual(0, state.updated_at)


class TestCurrentRollouts(unittest.TestCase):
    def make_log(self, data):
        return AuditLog(StringIO(data))

    def test_empty_log(self):
        self.assertEqual({}, self.make_log("").current_rollouts())

    def test_groups_active_flags_by_service(self):
        log = self.make_log("""\
1 billing new-checkout SET 25
2 billing invoice-search SET 70
3 identity passkeys SET 10
""")
        self.assertEqual(
            {
                "billing": {
                    "new-checkout": 25,
                    "invoice-search": 70,
                },
                "identity": {"passkeys": 10},
            },
            log.current_rollouts(),
        )

    def test_uses_latest_timestamp_when_out_of_order(self):
        log = self.make_log("""\
10 billing new-checkout SET 80
3 billing new-checkout SET 20
7 billing new-checkout SET 50
""")
        self.assertEqual(
            {"billing": {"new-checkout": 80}},
            log.current_rollouts(),
        )

    def test_same_timestamp_uses_later_log_event(self):
        log = self.make_log("""\
5 billing new-checkout SET 20
5 billing new-checkout SET 65
""")
        self.assertEqual(
            {"billing": {"new-checkout": 65}},
            log.current_rollouts(),
        )

    def test_delete_removes_flag(self):
        log = self.make_log("""\
1 billing new-checkout SET 25
2 billing invoice-search SET 70
3 billing new-checkout DELETE -
""")
        self.assertEqual(
            {"billing": {"invoice-search": 70}},
            log.current_rollouts(),
        )

    def test_newer_set_reactivates_deleted_flag(self):
        log = self.make_log("""\
1 billing new-checkout SET 25
5 billing new-checkout DELETE -
9 billing new-checkout SET 40
""")
        self.assertEqual(
            {"billing": {"new-checkout": 40}},
            log.current_rollouts(),
        )

    def test_older_set_does_not_reactivate_deleted_flag(self):
        log = self.make_log("""\
5 billing new-checkout DELETE -
2 billing new-checkout SET 90
""")
        self.assertEqual({}, log.current_rollouts())

    def test_set_zero_is_omitted(self):
        log = self.make_log("""\
1 billing new-checkout SET 0
2 identity passkeys SET 10
""")
        self.assertEqual(
            {"identity": {"passkeys": 10}},
            log.current_rollouts(),
        )

    def test_same_flag_name_in_different_services_is_independent(self):
        log = self.make_log("""\
1 billing redesign SET 20
2 identity redesign SET 80
3 billing redesign DELETE -
""")
        self.assertEqual(
            {"identity": {"redesign": 80}},
            log.current_rollouts(),
        )


class TestRolloutExposure(unittest.TestCase):
    def make_log(self, data):
        return AuditLog(StringIO(data))

    def test_empty_log(self):
        self.assertEqual(
            {}, self.make_log("").rollout_exposure_by_service(10)
        )

    def test_single_set_runs_until_end_time(self):
        log = self.make_log("2 billing new-checkout SET 25\n")
        self.assertEqual(
            {"billing": 200}, log.rollout_exposure_by_service(10)
        )

    def test_set_change_and_delete(self):
        log = self.make_log("""\
2 billing new-checkout SET 20
5 billing new-checkout SET 50
7 billing new-checkout DELETE -
""")
        self.assertEqual(
            {"billing": 160}, log.rollout_exposure_by_service(10)
        )

    def test_out_of_order_events_are_processed_chronologically(self):
        log = self.make_log("""\
7 billing new-checkout DELETE -
2 billing new-checkout SET 20
5 billing new-checkout SET 50
""")
        self.assertEqual(
            {"billing": 160}, log.rollout_exposure_by_service(10)
        )

    def test_same_timestamp_uses_later_log_event(self):
        log = self.make_log("""\
2 billing new-checkout SET 20
2 billing new-checkout SET 60
""")
        self.assertEqual(
            {"billing": 180}, log.rollout_exposure_by_service(5)
        )

    def test_multiple_flags_in_one_service_are_summed(self):
        log = self.make_log("""\
0 billing new-checkout SET 20
2 billing invoice-search SET 50
4 billing new-checkout DELETE -
""")
        self.assertEqual(
            {"billing": 280}, log.rollout_exposure_by_service(6)
        )

    def test_services_are_independent(self):
        log = self.make_log("""\
0 billing redesign SET 20
1 identity redesign SET 50
""")
        self.assertEqual(
            {"billing": 100, "identity": 200},
            log.rollout_exposure_by_service(5),
        )

    def test_events_after_end_time_are_ignored(self):
        log = self.make_log("""\
2 billing new-checkout SET 25
8 billing new-checkout SET 90
9 identity passkeys SET 100
""")
        self.assertEqual(
            {"billing": 75}, log.rollout_exposure_by_service(5)
        )

    def test_deleted_flag_can_be_reactivated(self):
        log = self.make_log("""\
0 billing new-checkout SET 20
2 billing new-checkout DELETE -
5 billing new-checkout SET 30
""")
        self.assertEqual(
            {"billing": 130}, log.rollout_exposure_by_service(8)
        )

    def test_zero_rollout_and_delete_produce_no_output(self):
        log = self.make_log("""\
0 billing new-checkout SET 0
2 identity passkeys DELETE -
""")
        self.assertEqual({}, log.rollout_exposure_by_service(8))

    def test_event_exactly_at_end_time_adds_no_exposure(self):
        log = self.make_log("5 billing new-checkout SET 100\n")
        self.assertEqual({}, log.rollout_exposure_by_service(5))


if __name__ == "__main__":
    unittest.main()
```

---

# Complete Test Inventory

| Part | Tests | Key coverage |
| --- | ---: | --- |
| Debugging | 9 | Parsing, validation, ownership, newer/equal/older timestamps, timestamp zero |
| Integration Part 1 | 9 | Empty input, grouping, out-of-order events, ties, delete, reactivation, zero rollout, composite identity |
| Integration Part 2 | 11 | Empty input, time intervals, changes, delete, out-of-order events, ties, aggregation, future events, reactivation, zero exposure |
| **Total** | **29** | Full runnable suite |

# Common Mistakes

- Treating timestamp `0` as missing state.
- Keying only by flag name and mixing services.
- Assuming the audit log is already chronological.
- Letting an older event overwrite newer current state.
- Using `>` instead of `>=` and violating the equal-timestamp rule.
- Returning deleted or `SET 0` flags.
- Calculating exposure with the new rollout instead of the previous rollout for an interval.
- Forgetting to accumulate from the last event through `end_time`.
- Including events after `end_time`.
- Calculating one combined timeline for all flags instead of independent timelines.
- Giving complexity without defining variables.

# Scoring Guide

| Area | Strong signal |
| --- | --- |
| Orientation | Explains parsing, validation, state, and aggregation clearly |
| Debugging | Reproduces the timestamp-zero failure and makes the smallest fix |
| Clarification | Confirms ordering, ties, deletes, reactivation, and output rules |
| Data structures | Uses composite-key dictionaries and per-flag event groups |
| Integration | Reuses `FeatureFlag.apply()` for current state and models time intervals correctly |
| Correctness | Handles stale, tied, deleted, future, and cross-service events |
| Testing | Runs all 29 tests and explains the cases that protect state transitions |
| Complexity | States `O(n)` for current state and `O(n log n)` for unordered exposure |
| Communication | Explains the state model before and during implementation |

# Interviewer Stopping Rule

End when the candidate has:

1. Fixed the timestamp-zero bug.
2. Passed all 9 debugging tests.
3. Implemented `current_rollouts()` and passed all 9 Part 1 tests.
4. Implemented `rollout_exposure_by_service()` and passed all 11 Part 2 tests.
5. Explained at least four edge cases.
6. Stated correct time and space complexity for both methods.
