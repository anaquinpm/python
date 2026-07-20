---
title: Type Hints and Annotations
tags: [type-hints, annotations, typing, mypy, pep484]
status: complete
source: Official Python docs, PEP 484, typing module
last_updated: 2026-07-20
---

# Type Hints and Annotations

Type hints allow specifying the expected data types of variables, function parameters, and return values. While Python remains dynamically typed at runtime (type hints do not enforce checks on execution), static analysis tools can parse them to catch bugs early.

## Variable and Function Annotations

Basic annotations can be added using the colon (`:`) syntax for types and the arrow (`->`) syntax for return values.

```python
# Variable Type Hint
age: int = 25
name: str = "Alice"
is_active: bool = True

# Function Type Hint
def greet(user_name: str) -> str:
    return f"Hello, {user_name}!"
```

## Generic Aliases and Unions (Modern Syntax)

Modern Python (3.10+) uses standard collections and the pipe (`|`) operator for union and optional types, replacing old `typing.Union` and `typing.Optional` formats.

```python
# List and Dictionary generics
scores: list[int] = [95, 87, 92]
user_roles: dict[str, str] = {"alice": "admin", "bob": "user"}

# Union Type (can be one of multiple types)
def process_id(uid: int | str) -> None:
    print(f"User ID: {uid}")

# Optional Type (can be a type or None)
def find_user(username: str) -> str | None:
    database = {"alice": "Alice Smith"}
    return database.get(username)  # returns str or None
```

## The `typing` Module

For more complex type constructs, the `typing` module offers helper types.

```python
from typing import Callable, Any, Sequence, TypeVar

# 1. Callable: Type hint for functions passed as arguments
def execute_operation(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)

# 2. Any: Disables static type checking for a variable
data: Any = "Could be anything"

# 3. Sequence: Supports list, tuple, etc. (read-only collections)
def print_first_element(items: Sequence[str]) -> None:
    if items:
        print(items[0])

# 4. TypeVar: Used to create generic functions
T = TypeVar('T')  # Generic Type Variable

def get_first(items: list[T]) -> T:
    return items[0]
```

## Static Type Checking (`mypy`)

`mypy` is an external static type checker for Python. Run it via the terminal to find type mismatches.

```bash
# Install mypy
pip install mypy

# Run static type check
mypy script.py
```

## Best Practices and Runtime Validation

1. **Do Not Trust Type Hints at Runtime**: Because Python ignores hints when running, always sanitize and validate user-supplied inputs explicitly.
   ```python
   # Type hint is not enough for untrusted inputs
   def create_user(age: int):
       if not isinstance(age, int) or age < 0:
           raise ValueError("Age must be a positive integer.")
   ```
2. **Pydantic**: For data validation and settings management, use third-party libraries like `Pydantic` which enforce type declarations at runtime.
