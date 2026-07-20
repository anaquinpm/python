---
title: Iterators and Generators
tags: [iterators, generators, yield, itertools]
status: complete
source: Official Python Tutorial Ch. 9.8-9.10, itertools docs
last_updated: 2026-07-20
---

# Iterators and Generators

Python utilizes iterators and generators to enable memory-efficient, lazy evaluation of sequences. This allows processing large datasets or streams of data without loading everything into memory.

## Iterables vs. Iterators

- **Iterable**: An object that can return an iterator (defines `__iter__()` or implements `__getitem__()`). Examples: `list`, `str`, `dict`, `set`.
- **Iterator**: An object representing a stream of data; it returns the next element when `next()` is called (defines `__next__()` and `__iter__()`).

```python
numbers = [1, 2, 3]          # Iterable
iterator = iter(numbers)     # Get the iterator

print(next(iterator))        # Output: 1
print(next(iterator))        # Output: 2
print(next(iterator))        # Output: 3
# Calling next(iterator) again raises StopIteration
```

## Custom Iterators

To make a custom class act as an iterator, implement both `__iter__()` and `__next__()`.

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

# Usage
for num in Countdown(3):
    print(num)  # Prints 3, then 2, then 1
```

## Generators and the `yield` Statement

Generators are a simple way to create iterators using functions. A function containing the `yield` statement becomes a generator function. When called, it returns a generator object without immediately executing the function.

Calling `next()` on the generator executes code until it reaches `yield`, yielding the value and pausing the execution state.

```python
def fibonacci(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Usage
fib_gen = fibonacci(5)
for val in fib_gen:
    print(val)  # Output: 0, 1, 1, 2, 3
```

### Generator Expressions

Similar to list comprehensions, generator expressions use parentheses instead of brackets and produce values lazily.

```python
# List comprehension (Loads all squares into memory)
squares_list = [x**2 for x in range(1000000)]

# Generator expression (Calculates on the fly)
squares_gen = (x**2 for x in range(1000000))
print(next(squares_gen))  # Output: 0
print(next(squares_gen))  # Output: 1
```

## The `itertools` Module

The standard library `itertools` module provides memory-efficient tools for working with iterators.

```python
import itertools

# 1. chain: Combine multiple iterables
combined = itertools.chain([1, 2], ['a', 'b'])
print(list(combined))  # Output: [1, 2, 'a', 'b']

# 2. islice: Slice an iterator (avoids converting to list first)
infinite_count = itertools.count(start=10, step=2)  # 10, 12, 14, 16...
sliced = itertools.islice(infinite_count, 3)
print(list(sliced))  # Output: [10, 12, 14]

# 3. cycle: Repeat an iterable infinitely
cycler = itertools.cycle(['A', 'B'])
print(next(cycler), next(cycler), next(cycler))  # Output: A B A
```

## Best Practices and Memory Optimization

1. **Use Generators for Files and I/O**: When processing large logs or files, yield lines or chunks instead of calling `readlines()` which loads the entire file into memory.
   ```python
   def read_large_file(file_path):
       with open(file_path, "r") as file:
           for line in file:
               yield line.strip()
   ```
2. **Resource Cleanup**: Generators that hold onto resources (like file descriptors or sockets) can be explicitly closed using the `.close()` method, which raises a `GeneratorExit` inside the generator.
