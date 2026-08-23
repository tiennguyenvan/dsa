### Coding Problem 2 - Time-Based Key-Value Store

Implement:

```python
class TimeMap:
    def __init__(self):
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        pass

    def get(self, key: str, timestamp: int) -> str:
        pass
```

`set()` stores a value at a timestamp.

`get()` returns the value with the **largest stored timestamp ≤ the requested timestamp**. Return `""` if none exists.

For each key, timestamps passed to `set()` are strictly increasing.

Example:

```python
time_map = TimeMap()

time_map.set("foo", "bar", 1)

assert time_map.get("foo", 1) == "bar"
assert time_map.get("foo", 3) == "bar"

time_map.set("foo", "bar2", 4)

assert time_map.get("foo", 4) == "bar2"
assert time_map.get("foo", 5) == "bar2"
assert time_map.get("foo", 0) == ""
```

Please explain your approach before coding.
