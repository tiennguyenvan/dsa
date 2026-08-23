# Karat Obstacle Course Practice Interview

Based on: [Coding Question on Karat — Interview Experience](https://leetcode.com/discuss/post/5085876/coding-question-on-karat-interview-expie-luc8/)

> Note: This is a Python adaptation of the Java question. The reported code and narrative are not fully consistent about the original bug, so this version includes an intentional `RunCollection.personal_best()` bug that produces the described failing test while preserving the reported progressive tasks.

## Format

- Duration: 50 minutes
- Language: Python
- Structure: one existing codebase for all stages
- Part 1: orientation and debugging
- Part 2: implement `best_of_bests()`
- Part 3: implement `chance_of_personal_best()` using simulation

## Interviewer rules

- Give one prompt at a time.
- Do not reveal later requirements early.
- Let the candidate run the code and think aloud.
- Ask for an approach and complexity before substantial coding.
- Answer only the clarification questions relevant to the current part.
- If the candidate is stuck for 2–3 minutes, give the smallest listed hint.

## Candidate-visible initial code

```python
import math
import random
import unittest


class Course:
    def __init__(self, title, obstacle_count):
        self.title = title
        self.obstacle_count = obstacle_count

    def __eq__(self, other):
        return (
            isinstance(other, Course)
            and self.title == other.title
            and self.obstacle_count == other.obstacle_count
        )

    def __hash__(self):
        return hash((self.title, self.obstacle_count))


class Run:
    def __init__(self, course):
        self.course = course
        self.complete = False
        self.obstacle_times = []

    def add_obstacle_time(self, obstacle_time):
        if self.complete:
            raise ValueError("Cannot add an obstacle time to a complete run")

        self.obstacle_times.append(obstacle_time)

        if len(self.obstacle_times) == self.course.obstacle_count:
            self.complete = True

    def get_run_time(self):
        if not self.complete:
            return math.inf

        return sum(self.obstacle_times)


class RunCollection:
    def __init__(self, course):
        self.course = course
        self.runs = []

    def get_num_runs(self):
        return len(self.runs)

    def add_run(self, run):
        if run.course != self.course:
            raise ValueError("Run course does not match collection course")

        self.runs.append(run)

    def personal_best(self):
        if not self.runs:
            return math.inf

        return min(sum(run.obstacle_times) for run in self.runs)

    def best_of_bests(self):
        pass

    def chance_of_personal_best(self, test_run):
        pass


def make_run_collection(course, obstacle_data):
    collection = RunCollection(course)

    for run_data in obstacle_data:
        run = Run(course)

        for obstacle_time in run_data:
            run.add_obstacle_time(obstacle_time)

        collection.add_run(run)

    return collection


class TestObstacleCourse(unittest.TestCase):
    def test_run(self):
        course = Course("Test course", 2)
        run = Run(course)

        run.add_obstacle_time(3)
        self.assertFalse(run.complete)

        run.add_obstacle_time(5)
        self.assertTrue(run.complete)
        self.assertEqual([3, 5], run.obstacle_times)
        self.assertEqual(8, run.get_run_time())

        with self.assertRaises(ValueError):
            run.add_obstacle_time(4)

    def test_run_collection(self):
        # Obstacles: O1 O2 O3 O4
        # Run 1:     3  4  5  6  = 18
        # Run 2:     4  4  4  5  = 17
        # Run 3:     5  5  3     = incomplete
        obstacle_data = [
            [3, 4, 5, 6],
            [4, 4, 4, 5],
            [5, 5, 3],
        ]
        course = Course("Test course", 4)
        collection = make_run_collection(course, obstacle_data)

        self.assertEqual(3, collection.get_num_runs())
        self.assertEqual(17, collection.personal_best())

    def test_chance_of_personal_best(self):
        obstacle_data = [
            [32, 37],
            [31, 29, 34, 25, 25, 39],
            [25, 34, 38, 24, 26, 39, 33],
            [39, 21, 39, 34, 39, 29, 31, 22, 28, 20],
            [23, 22, 35, 33, 36, 21, 29, 37, 24, 34],
            [28, 34, 28, 22, 40, 28, 31, 33, 25, 20],
            [20, 38, 40, 28, 34, 22],
            [36, 39, 20, 32, 38, 24, 22],
            [40, 20, 21, 37, 32, 30, 40, 25, 37, 30],
            [21, 35, 30, 37, 32, 40, 26, 29, 29],
        ]

        course = Course("Test Course", 10)
        collection = make_run_collection(course, obstacle_data)

        test_run = Run(course)
        test_run.add_obstacle_time(19)
        test_run.add_obstacle_time(19)
        test_run.add_obstacle_time(19)

        chance = collection.chance_of_personal_best(test_run)

        print(chance)
        self.assertTrue(
            0.92813 <= chance <= 0.96813,
            f"chance should be between 0.92813 and 0.96813, was {chance}",
        )

if __name__ == "__main__":
    unittest.main()
```

## Incremental interview script

### 0:00–4:00 — Codebase orientation

**Interviewer instruction**

> We collect times for racers completing obstacle courses. Please read the code and explain the relationship among `Course`, `Run`, and `RunCollection`. You may run the code.

**Expected interviewee response**

- `Course` defines the course identity and number of obstacles.
- `Run` stores one attempt and its sequential obstacle times.
- A run becomes complete when its number of times equals the obstacle count.
- `get_run_time()` returns infinity for an incomplete run so it cannot become a personal best.
- `RunCollection` stores runs belonging to one course and calculates collection-level statistics.
- `make_run_collection()` is a test-data helper.
- The tests verify state transitions, total run time, invalid additions, number of runs, and personal best.

**Evaluation**

- Understands the domain model and state transitions.
- Notices the special meaning of `math.inf`.
- Identifies that incomplete runs may still matter for later per-obstacle statistics.

### 4:00–11:00 — Debug `RunCollection`

**Interviewer instruction**

> The `RunCollection` test is failing. Diagnose the failure and make the smallest correct fix inside `RunCollection`.

**Expected interviewee investigation**

1. Run the tests.
2. Observe that `personal_best()` returns `13` instead of `17`.
3. Identify that the incomplete run `[5, 5, 3]` is being treated as a completed 13-second run.
4. Use the existing `Run.get_run_time()` behavior or explicitly filter complete runs.

**Expected fix**

```python
def personal_best(self):
    return min(
        (run.get_run_time() for run in self.runs),
        default=math.inf,
    )
```

**Expected explanation**

- `Run` already owns the rule for whether its time is eligible.
- Reusing `get_run_time()` avoids duplicating completion logic.
- An empty collection or a collection with no complete run returns infinity.

**Small hint if needed**

> Compare the incomplete run's partial sum with the expected personal best.

### 11:00–14:00 — Debugging follow-up

**Interviewer instruction**

> Would filtering with `if run.complete` also work? Which version do you prefer?

**Expected interviewee response**

- Both can produce the correct result.
- Calling `get_run_time()` is preferable because eligibility behavior belongs to `Run`.
- Explicit filtering may be clearer if the domain later changes how incomplete runs are represented.
- The important point is to avoid counting partial totals as completed personal bests.

### 14:00–17:00 — Reveal `best_of_bests`

**Interviewer instruction**

> Implement `best_of_bests()`. It represents the fastest theoretical run: take the fastest observed time for each obstacle across all runs, including incomplete runs, and sum those times. Add a test.

### 17:00–20:00 — Clarify and design `best_of_bests`

**Expected interviewee questions**

- Do obstacle times correspond to their list indices?
- Should incomplete runs contribute times for obstacles they reached?
- What happens if no run contains a time for a particular obstacle?
- What should an empty collection return?

**Interviewer answers for this practice**

- Yes, index `i` represents obstacle `i`.
- Yes, use every recorded time, including times from incomplete runs.
- Assume every obstacle has at least one observed time in the main tests.
- Return infinity if any obstacle has no observed time.

**Expected interviewee design**

> I will keep one minimum per obstacle. I will scan every recorded time in every run and update the minimum for its obstacle index. If every obstacle has a value, I will return their sum.

**Expected complexity**

- Time: `O(t)`, where `t` is the total number of recorded obstacle times.
- Space: `O(k)`, where `k` is the number of obstacles.

### 20:00–27:00 — Implement and test `best_of_bests`

**Expected implementation**

```python
def best_of_bests(self):
    best_times = [math.inf] * self.course.obstacle_count

    for run in self.runs:
        for index, obstacle_time in enumerate(run.obstacle_times):
            best_times[index] = min(best_times[index], obstacle_time)

    if any(time == math.inf for time in best_times):
        return math.inf

    return sum(best_times)
```

**Expected test**

```python
def test_best_of_bests(self):
    course = Course("Test course", 4)
    collection = make_run_collection(
        course,
        [
            [3, 4, 5, 6],
            [4, 4, 4, 5],
            [5, 5, 3],
        ],
    )

    # Minimums: 3 + 4 + 3 + 5
    self.assertEqual(15, collection.best_of_bests())
```

**Interviewer follow-up**

> Why must the incomplete third run be included?

**Expected response**

> It contains a valid observed time of `3` for obstacle 3, even though it has no time for obstacle 4. `best_of_bests()` combines individual obstacle performance, not only complete-run totals.

### 27:00–31:00 — Reveal `chance_of_personal_best`

**Interviewer instruction**

> Implement `chance_of_personal_best(test_run)` using 10,000 simulation trials.
>
> For each unfinished obstacle in `test_run`, randomly choose a time previously observed for that same obstacle. Include observations from incomplete runs. Count a trial as successful when the simulated total is less than or equal to the current personal best. Return the successful fraction.

### 31:00–35:00 — Clarify and design the simulation

**Expected interviewee questions**

- Does `test_run` have to belong to the same course?
- Does matching the personal best count as success?
- Are samples selected independently for each remaining obstacle?
- Should the simulation mutate `test_run`?
- What happens if a remaining obstacle has no historical samples?

**Interviewer answers for this practice**

- Yes; reject a different course.
- Yes; use `<= personal_best`.
- Yes; each remaining obstacle is sampled independently from its own observations.
- No; do not mutate the supplied run.
- Return `0.0` when simulation is impossible because a remaining obstacle has no samples.

**Expected interviewee design**

1. Build a list of historical samples for every obstacle index.
2. Store the sum already completed by `test_run`.
3. Run 10,000 trials.
4. For each trial, sample one value for each remaining obstacle.
5. Compare the simulated total with `personal_best()`.
6. Return successes divided by 10,000.

### 35:00–44:00 — Implement the simulation

**Expected implementation**

```python
def chance_of_personal_best(self, test_run):
    if test_run.course != self.course:
        raise ValueError("Run course does not match collection course")

    samples = [
        [] for _ in range(self.course.obstacle_count)
    ]

    for run in self.runs:
        for index, obstacle_time in enumerate(run.obstacle_times):
            samples[index].append(obstacle_time)

    start_index = len(test_run.obstacle_times)

    if any(not samples[index]
           for index in range(start_index, self.course.obstacle_count)):
        return 0.0

    personal_best = self.personal_best()
    completed_time = sum(test_run.obstacle_times)
    successes = 0
    trials = 10_000

    for _ in range(trials):
        simulated_time = completed_time

        for index in range(start_index, self.course.obstacle_count):
            simulated_time += random.choice(samples[index])

        if simulated_time <= personal_best:
            successes += 1

    return successes / trials
```

**What a strong candidate explains**

- Historical samples are grouped by obstacle, not by complete run.
- The existing `test_run` object is never changed.
- Duplicate observed times remain in the sample pool because they represent frequency.
- Equality counts as a personal best.
- Seeding randomness in tests makes failures reproducible.

### 44:00–48:00 — Test the simulation

**Expected test 1: probability 0.5**

```python
def test_chance_of_personal_best_half(self):
    random.seed(0)
    course = Course("Test course", 3)
    collection = make_run_collection(
        course,
        [
            [3, 3, 2],
            [3, 3, 3],
        ],
    )

    test_run = Run(course)
    test_run.add_obstacle_time(3)
    test_run.add_obstacle_time(3)

    chance = collection.chance_of_personal_best(test_run)
    self.assertTrue(0.48 <= chance <= 0.52)
```

**Expected reasoning**

- Personal best is `8`.
- Current total is `6`.
- The last obstacle is sampled from `[2, 3]`.
- Only choosing `2` produces a total of `8`, so probability is `1/2`.

**Expected test 2: probability 5/6**

```python
def test_chance_of_personal_best_five_sixths(self):
    random.seed(0)
    course = Course("Test course", 4)
    collection = make_run_collection(
        course,
        [
            [3, 3, 2, 3],
            [3, 3, 3, 2],
            [5, 5, 2],
        ],
    )

    test_run = Run(course)
    test_run.add_obstacle_time(3)
    test_run.add_obstacle_time(3)

    chance = collection.chance_of_personal_best(test_run)
    self.assertTrue(0.813 <= chance <= 0.853)
```

**Expected reasoning**

- Personal best is `11`.
- Obstacle 3 samples are `[2, 3, 2]`.
- Obstacle 4 samples are `[3, 2]`.
- Only the combination `3 + 3` fails.
- Its probability is `1/3 × 1/2 = 1/6`.
- Success probability is `1 - 1/6 = 5/6`.

### 48:00–50:00 — Complexity and final follow-up

**Interviewer instruction**

> State the time and space complexity. How could you test this without flaky randomness?

**Expected interviewee response**

Let:

- `t` = total recorded historical obstacle times
- `r` = number of remaining obstacles in `test_run`
- `s` = number of simulation trials, fixed at 10,000

Then:

- Building samples: `O(t)` time and `O(t)` space.
- Simulation: `O(s × r)` time.
- Total: `O(t + s × r)` time and `O(t)` space.

For deterministic tests:

- Seed the random generator.
- Better: inject a random generator or sampler dependency.
- For small datasets, calculate the exact probability and only use simulation for the production requirement.

## Optional senior-level follow-ups

Ask these only if time remains.

### Follow-up A — Early termination

> Can any simulation work be skipped?

**Expected response**

- If the completed time already exceeds the personal best, return `0.0` because all obstacle times are positive.
- While simulating a trial, stop adding once its total exceeds the personal best.

### Follow-up B — Exact probability

> How could you compute the probability without simulation?

**Expected response**

- Use dynamic programming over possible accumulated totals.
- For each remaining obstacle, combine the current sum distribution with that obstacle's empirical frequency distribution.
- Sum probabilities for totals `<= personal_best`.
- This avoids sampling error but can be expensive when time values or totals are large.

### Follow-up C — Repeated queries

> How would you optimize many probability queries against the same collection?

**Expected response**

- Precompute samples or frequency maps by obstacle.
- Cache the current personal best.
- Invalidate cached statistics only when a new run is added.

## Common mistakes

- Allowing an incomplete run's partial total to become the personal best.
- Excluding incomplete runs from per-obstacle sample pools.
- Taking the minimum complete run for `best_of_bests()` instead of one minimum per obstacle.
- Sampling from all times instead of times for the same obstacle index.
- Mutating `test_run` during simulation.
- Using `<` instead of `<=` for matching a personal best.
- Removing duplicate times from samples and changing their empirical frequencies.
- Running only one random completion instead of 10,000 trials.
- Writing probabilistic tests with an unrealistically narrow tolerance.

## Scoring guide

| Area | Strong signal |
| --- | --- |
| Orientation | Explains object responsibilities and incomplete-run behavior |
| Debugging | Reproduces `13` vs `17` and fixes the correct abstraction |
| Best of bests | Finds one minimum per obstacle across all recorded data |
| Clarification | Confirms index meaning, incomplete data, equality, and mutation rules |
| Simulation | Samples independently from the correct obstacle distributions |
| Testing | Derives `1/2` and `5/6`, then uses reasonable tolerance |
| Complexity | Gives `O(t + s × r)` time and `O(t)` space with defined variables |
| Code quality | Clear names, no mutation of input, and explicit validation |

## Interviewer stopping rule

End when the candidate has:

1. Fixed `personal_best()`.
2. Implemented and tested `best_of_bests()`.
3. Implemented the 10,000-trial probability simulation.
4. Explained at least three edge cases.
5. Stated correct complexity.

