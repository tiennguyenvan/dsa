# Karat IC3 Delivery Order Manager — Reconstructed Real Interview

Reconstructed from Tim Nguyen's real Karat IC3 coding interview on August 24, 2026.

> The three main tasks and domain objects come from the candidate's memory. Exact field names, sample values, and edge-case rules were reconstructed where the original details were not remembered.

## Remembered interview structure

- **Question 1:** Debug `OrderManager.get_stats()` because `PREPARING` is missing from active orders and `CANCELED` is missing from closed orders.
- **Question 2:** Add a `Delivery` to an existing order.
- **Question 3:** Calculate average delivery time per restaurant.

## Reconstructed assumptions

- `DELIVERED` and `CANCELED` are closed statuses.
- `PLACED`, `PREPARING`, and `OUT_TO_DELIVER` are active statuses.
- `add_delivery()` returns `False` only when the order does not exist.
- One delivery is stored per order.
- A delivery is complete only when both start and end times exist.
- Incomplete deliveries are excluded from restaurant averages.
- Restaurants without completed deliveries are omitted from the result.

## Format

- Duration: 50 minutes
- Language: Python
- Target: IC3
- Part 1: codebase orientation and debugging
- Part 2: add delivery data
- Part 3: aggregate delivery durations by restaurant

## Interviewer rules

- Reveal one question at a time.
- Let the candidate read and run the existing code first.
- Ask for an approach before substantial implementation.
- Answer only clarifications relevant to the current question.
- Do not reveal Question 2 or Question 3 during debugging.
- If the candidate is stuck for 2–3 minutes, give only the smallest listed hint.
- Evaluate correctness, testing, code clarity, and communication.

# Candidate Starter File

```python
import unittest
from enum import Enum
from io import StringIO


class OrderStatus(Enum):
    PLACED = "PLACED"
    PREPARING = "PREPARING"
    OUT_TO_DELIVER = "OUT_TO_DELIVER"
    DELIVERED = "DELIVERED"
    CANCELED = "CANCELED"


class Order:
    def __init__(self, line):
        tokens = line.split()

        if len(tokens) != 3:
            raise ValueError(
                "Expected: order_id restaurant_id status"
            )

        self.order_id = tokens[0]
        self.restaurant_id = tokens[1]
        self.status = OrderStatus(tokens[2])


class Delivery:
    def __init__(self, delivery_id, start_time, end_time):
        self.delivery_id = delivery_id
        self.start_time = start_time
        self.end_time = end_time

    def get_delivery_minutes(self):
        if self.start_time is None or self.end_time is None:
            return None

        return self.end_time - self.start_time


class OrderManager:
    def __init__(self, reader):
        self.orders = {}
        self.deliveries = {}

        self.total = 0
        self.active = 0
        self.closed = 0

        for line in reader:
            line = line.strip()

            if not line:
                continue

            order = Order(line)
            self.orders[order.order_id] = order
            self.total += 1

            if order.status in {
                OrderStatus.PLACED,
                OrderStatus.OUT_TO_DELIVER,
            }:
                self.active += 1
            elif order.status == OrderStatus.DELIVERED:
                self.closed += 1

    def get_stats(self):
        return {
            "total": self.total,
            "active": self.active,
            "closed": self.closed,
        }

    def add_delivery(self, order_id, delivery):
        pass

    def average_delivery_per_restaurant(self):
        pass


ORDERS = """\
order-1 restaurant-a PLACED
order-2 restaurant-a DELIVERED
order-3 restaurant-b PREPARING
order-4 restaurant-b CANCELED
order-5 restaurant-a OUT_TO_DELIVER
"""


class TestOrderManager(unittest.TestCase):
    def test_order(self):
        order = Order("order-10 restaurant-x PREPARING")

        self.assertEqual("order-10", order.order_id)
        self.assertEqual("restaurant-x", order.restaurant_id)
        self.assertEqual(OrderStatus.PREPARING, order.status)

    def test_get_stats(self):
        manager = OrderManager(StringIO(ORDERS))

        self.assertEqual(
            {
                "total": 5,
                "active": 3,
                "closed": 2,
            },
            manager.get_stats(),
        )


if __name__ == "__main__":
    unittest.main()
```

# Incremental Interview Script

## 0:00–4:00 — Introduction and codebase orientation

### Interviewer instruction

> This program loads restaurant orders and reports summary statistics. Read the code and explain the responsibilities of `OrderStatus`, `Order`, `Delivery`, and `OrderManager`. Then describe how one input line moves through the program. Think aloud.

### Expected interviewee response

- `OrderStatus` defines the valid lifecycle states.
- `Order` parses one order line into an order ID, restaurant ID, and enum status.
- `Delivery` represents one delivery and calculates its duration when complete.
- `OrderManager` loads orders, indexes them by order ID, and maintains statistics.
- `StringIO` makes the sample string behave like a file.
- `self.orders` provides direct order lookup by ID.

### Evaluation

- Navigates unfamiliar code before editing.
- Recognizes terminal and nonterminal order states.
- Understands why orders are stored in a dictionary.

## 4:00–11:00 — Question 1: run and debug

### Interviewer instruction

> Run the tests. Both the active and closed counts are wrong. Diagnose the problem and make the smallest safe fix.

### Expected investigation

1. Run the suite and inspect the failing expected and actual dictionaries.
2. Confirm that `total` is correct.
3. Compare every enum value with the statuses handled by the counting code.
4. Notice that two statuses are missing:

```python
active: PLACED, OUT_TO_DELIVER
closed: DELIVERED
```

`PREPARING` is not counted as active, and `CANCELED` is not counted as closed.

### Expected fix

```python
if order.status in {
    OrderStatus.DELIVERED,
    OrderStatus.CANCELED,
}:
    self.closed += 1
else:
    self.active += 1
```

An equivalent correct condition is:

```python
if (
    order.status != OrderStatus.DELIVERED
    and order.status != OrderStatus.CANCELED
):
    self.active += 1
else:
    self.closed += 1
```

### Small hint if needed

> Compare the enum values with every status handled by the two counters.

## 11:00–14:00 — Debugging follow-up

### Interviewer instruction

> Why is grouping terminal statuses safer than listing only one closed status?

### Expected interviewee response

- The original code forgot valid enum values.
- A terminal-status set defines the closed business states in one place.
- Every nonterminal status can then be counted as active.

```python
CLOSED_STATUSES = {
    OrderStatus.DELIVERED,
    OrderStatus.CANCELED,
}
```

### Optional follow-up

> What happens if a new terminal status such as `REFUNDED` is added later?

Expected answer: update one closed-status collection rather than duplicating conditions.

## 14:00–17:00 — Reveal Question 2

### Interviewer instruction

> Implement `add_delivery(order_id, delivery)`.
>
> If the order exists, associate the delivery with it and return `True`. If the order does not exist, make no change and return `False`.

## 17:00–20:00 — Clarify and design Question 2

### Expected interviewee questions

- How are deliveries stored?
- Can one order have more than one delivery?
- What happens if another delivery is added for the same order?
- Do we validate the order status?
- Can `delivery` be `None`?

### Interviewer answers for this reconstruction

- Store deliveries in `self.deliveries` keyed by order ID.
- One delivery is stored per order.
- A later valid call replaces the earlier delivery.
- Do not validate order status for this task.
- Assume `delivery` is a valid `Delivery` instance.

### Expected design

> I will first check `self.orders`. If the ID is absent, I return `False` without changing state. Otherwise, I assign the delivery in `self.deliveries` and return `True`.

## 20:00–28:00 — Test and implement Question 2

### Tests revealed to the candidate

```python
def test_delivery_duration(self):
    delivery = Delivery("delivery-1", 100, 125)
    self.assertEqual(25, delivery.get_delivery_minutes())

    incomplete = Delivery("delivery-2", 100, None)
    self.assertIsNone(incomplete.get_delivery_minutes())

def test_add_delivery(self):
    manager = OrderManager(StringIO(ORDERS))
    delivery = Delivery("delivery-1", 100, 125)

    self.assertTrue(manager.add_delivery("order-2", delivery))
    self.assertIs(delivery, manager.deliveries["order-2"])

def test_add_delivery_unknown_order(self):
    manager = OrderManager(StringIO(ORDERS))
    delivery = Delivery("delivery-x", 100, 125)

    self.assertFalse(manager.add_delivery("missing", delivery))
    self.assertNotIn("missing", manager.deliveries)
```

### Expected implementation

```python
def add_delivery(self, order_id, delivery):
    if order_id not in self.orders:
        return False

    self.deliveries[order_id] = delivery
    return True
```

### Evaluation

- Checks existence before mutation.
- Returns the required Boolean on both paths.
- Uses existing dictionaries rather than scanning all orders.
- Does not add unrequested status restrictions.

### Small hint if needed

> Which existing collection gives you direct access to an order by ID?

## 28:00–31:00 — Reveal Question 3

### Interviewer instruction

> Implement `average_delivery_per_restaurant()`.
>
> Return a dictionary mapping each restaurant ID to its average completed delivery time in minutes.

Example:

```python
{
    "restaurant-a": 25.0,
    "restaurant-b": 40.0,
}
```

## 31:00–35:00 — Clarify and design Question 3

### Expected interviewee questions

- Should incomplete deliveries be ignored?
- Should restaurants without deliveries appear?
- Should restaurants with only incomplete deliveries appear?
- Is the return value a float?
- Does every stored delivery have a valid order?

### Interviewer answers for this reconstruction

- Ignore incomplete deliveries whose duration is `None`.
- Omit restaurants without completed deliveries.
- Therefore, omit restaurants with only incomplete deliveries.
- Normal Python division is acceptable, so averages are floats.
- Yes. `add_delivery()` guarantees that stored deliveries reference existing orders.

### Expected design

> I will scan the deliveries once. For every completed delivery, I will find its order, get the restaurant ID, and maintain a total duration and count for that restaurant. Then I will build the result by dividing each total by its count.

## 35:00–45:00 — Test and implement Question 3

### Tests revealed to the candidate

```python
def test_average_delivery_per_restaurant(self):
    manager = OrderManager(StringIO(ORDERS))

    manager.add_delivery(
        "order-1",
        Delivery("delivery-1", 100, 120),
    )
    manager.add_delivery(
        "order-2",
        Delivery("delivery-2", 200, 230),
    )
    manager.add_delivery(
        "order-3",
        Delivery("delivery-3", 300, 340),
    )

    self.assertEqual(
        {
            "restaurant-a": 25.0,
            "restaurant-b": 40.0,
        },
        manager.average_delivery_per_restaurant(),
    )

def test_average_ignores_incomplete_deliveries(self):
    manager = OrderManager(StringIO(ORDERS))

    manager.add_delivery(
        "order-1",
        Delivery("delivery-1", 100, 120),
    )
    manager.add_delivery(
        "order-2",
        Delivery("delivery-2", 200, None),
    )
    manager.add_delivery(
        "order-3",
        Delivery("delivery-3", None, None),
    )

    self.assertEqual(
        {"restaurant-a": 20.0},
        manager.average_delivery_per_restaurant(),
    )

def test_average_with_no_deliveries(self):
    manager = OrderManager(StringIO(ORDERS))

    self.assertEqual({}, manager.average_delivery_per_restaurant())
```

### Expected implementation

```python
def average_delivery_per_restaurant(self):
    totals = {}
    counts = {}

    for order_id, delivery in self.deliveries.items():
        duration = delivery.get_delivery_minutes()

        if duration is None:
            continue

        restaurant_id = self.orders[order_id].restaurant_id

        if restaurant_id not in totals:
            totals[restaurant_id] = 0
            counts[restaurant_id] = 0

        totals[restaurant_id] += duration
        counts[restaurant_id] += 1

    return {
        restaurant_id: totals[restaurant_id] / counts[restaurant_id]
        for restaurant_id in totals
    }
```

### Acceptable alternative

Store `[total, count]` together:

```python
def average_delivery_per_restaurant(self):
    stats = {}

    for order_id, delivery in self.deliveries.items():
        duration = delivery.get_delivery_minutes()

        if duration is None:
            continue

        restaurant_id = self.orders[order_id].restaurant_id

        if restaurant_id not in stats:
            stats[restaurant_id] = [0, 0]

        stats[restaurant_id][0] += duration
        stats[restaurant_id][1] += 1

    return {
        restaurant_id: total / count
        for restaurant_id, (total, count) in stats.items()
    }
```

### Small hint if needed

> An average requires two values per restaurant. What are they?

## 45:00–50:00 — Edge cases and testing discussion

### Interviewer instruction

> What additional tests would you add before shipping this code?

### Expected interviewee response

- Empty order file.
- All orders active.
- All orders closed.
- Every `OrderStatus` value.
- Blank lines in the file.
- Unknown order passed to `add_delivery()`.
- Replacement delivery for the same order.
- No deliveries.
- One completed delivery.
- Multiple deliveries across multiple restaurants.
- Incomplete delivery.
- Zero-minute delivery, such as start `100` and end `100`.

### Important zero-duration observation

The code must use:

```python
if duration is None:
```

It must not use:

```python
if not duration:
```

A duration of `0` is complete and valid even though it is falsey.

# Complete Reference Implementation

```python
from enum import Enum


class OrderStatus(Enum):
    PLACED = "PLACED"
    PREPARING = "PREPARING"
    OUT_TO_DELIVER = "OUT_TO_DELIVER"
    DELIVERED = "DELIVERED"
    CANCELED = "CANCELED"


CLOSED_STATUSES = {
    OrderStatus.DELIVERED,
    OrderStatus.CANCELED,
}


class Order:
    def __init__(self, line):
        tokens = line.split()

        if len(tokens) != 3:
            raise ValueError(
                "Expected: order_id restaurant_id status"
            )

        self.order_id = tokens[0]
        self.restaurant_id = tokens[1]
        self.status = OrderStatus(tokens[2])


class Delivery:
    def __init__(self, delivery_id, start_time, end_time):
        self.delivery_id = delivery_id
        self.start_time = start_time
        self.end_time = end_time

    def get_delivery_minutes(self):
        if self.start_time is None or self.end_time is None:
            return None

        return self.end_time - self.start_time


class OrderManager:
    def __init__(self, reader):
        self.orders = {}
        self.deliveries = {}

        self.total = 0
        self.active = 0
        self.closed = 0

        for line in reader:
            line = line.strip()

            if not line:
                continue

            order = Order(line)
            self.orders[order.order_id] = order
            self.total += 1

            if order.status in CLOSED_STATUSES:
                self.closed += 1
            else:
                self.active += 1

    def get_stats(self):
        return {
            "total": self.total,
            "active": self.active,
            "closed": self.closed,
        }

    def add_delivery(self, order_id, delivery):
        if order_id not in self.orders:
            return False

        self.deliveries[order_id] = delivery
        return True

    def average_delivery_per_restaurant(self):
        stats = {}

        for order_id, delivery in self.deliveries.items():
            duration = delivery.get_delivery_minutes()

            if duration is None:
                continue

            restaurant_id = self.orders[order_id].restaurant_id

            if restaurant_id not in stats:
                stats[restaurant_id] = [0, 0]

            stats[restaurant_id][0] += duration
            stats[restaurant_id][1] += 1

        return {
            restaurant_id: total / count
            for restaurant_id, (total, count) in stats.items()
        }
```

# Complete Test Inventory

## Parsing and loading

- Parses order ID, restaurant ID, and enum status.
- Rejects malformed lines.
- Ignores blank lines.
- Loads all orders into a dictionary.

## Question 1

- Empty manager returns zero for all statistics.
- All active statuses increment `active`.
- `DELIVERED` increments `closed`.
- `CANCELED` increments `closed`.
- Mixed statuses produce correct total, active, and closed counts.

## Question 2

- Existing order returns `True` and stores its delivery.
- Unknown order returns `False` and makes no change.
- A later delivery replaces the earlier delivery for the same order.

## Question 3

- No deliveries returns `{}`.
- One completed delivery produces one average.
- Multiple deliveries for one restaurant are averaged.
- Multiple restaurants are grouped independently.
- Incomplete deliveries are ignored.
- Restaurants with only incomplete deliveries are omitted.
- A zero-minute completed delivery is included.

# Common Mistakes

- Forgetting to handle every enum status.
- Fixing expected test values instead of the production condition.
- Scanning all orders inside `add_delivery()` instead of using the dictionary.
- Adding a delivery before checking whether the order exists.
- Forgetting to associate the delivery with its order.
- Averaging globally instead of grouping by restaurant.
- Dividing each duration before computing the restaurant total.
- Using one global count for every restaurant.
- Treating `0` minutes as incomplete.
- Including incomplete deliveries in the count.
- Returning totals rather than averages.

# Scoring Guide

## Strong IC3

- Explains the codebase clearly before editing.
- Finds the Boolean logic bug quickly.
- Makes the smallest correct fix and reruns tests.
- Clarifies missing delivery rules instead of guessing silently.
- Implements `add_delivery()` with direct dictionary operations.
- Correctly groups completed durations by restaurant.
- Tests empty, missing, incomplete, zero-duration, and multi-group cases.
- Communicates continuously without overexplaining.

## Borderline IC3

- Solves all tasks but needs one or two small hints.
- Misses an edge case but corrects it after a failing test.
- Produces working code with some duplication or unclear naming.

## Below IC3

- Cannot isolate the Question 1 failure.
- Changes unrelated code during debugging.
- Mutates state for an unknown order.
- Cannot connect a delivery to its order and restaurant.
- Computes the wrong aggregation or count.
- Does not test the changes.

# Interviewer Stopping Rule

- Stop after Question 1 if the candidate cannot debug the Boolean condition with a small hint.
- Continue to Question 2 if the debugging fix is correct and explained.
- Continue to Question 3 if `add_delivery()` handles both existing and missing orders.

# Short Candidate Summary

The interview tests three practical skills:

1. Debug a state-counting condition.
2. Safely connect related domain objects using dictionary lookup.
3. Perform grouped aggregation using total and count per key.
