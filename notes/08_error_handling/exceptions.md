---
title: Exception Handling
tags: [fundamentals, error-handling, exceptions, try-except]
status: draft
source: General Reference
last_updated: 2026-07-10
---

# Exception Handling

Python uses exceptions to manage errors and exceptional events during program execution.

## Basic Syntax

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError as e:
    # Code to handle the specific exception
    print("Cannot divide by zero:", e)
else:
    # Optional block: executed only if no exceptions were raised
    print("Success! Result is:", result)
finally:
    # Optional block: always executed, regardless of whether an exception occurred
    print("Cleaning up resources.")
```

## Raising Exceptions

You can manually raise exceptions using the `raise` statement:

```python
raise ValueError("Invalid value provided.")
```

## Defining Custom Exceptions

To create custom exceptions, inherit from the built-in `Exception` class:

```python
class MyCustomError(Exception):
    """Custom exception class."""
    pass
```
