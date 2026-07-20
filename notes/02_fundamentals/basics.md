---
title: Python Basics
tags: [fundamentals, basics, syntax, variables, types, security]
status: complete
source: The Quick Python Book, Ch. 4
last_updated: 2026-07-20
---

# Python Basics

## Indentation and Block Structure

In Python, spaces and indentation are used to define block structures.

```python
n = 5
while n > 0:
    n -= 1         # Indented lines belong to the while loop block
```

## Comments

The `#` symbol marks the start of a comment, which is not executed by the interpreter. The exception is when `#` is inside a string literal.

```python
# This is a comment at the beginning of a line
n = 4     ## This is an inline comment
comment = "# Within this string, the symbol is just text"
```

## Variables and Assignments

Variables are created automatically upon their first assignment.

```python
x = 5       # Binds the value 5 to the variable x
```

Variables are tags or labels that point to an object in the interpreter's namespace. An object can be referenced by multiple variables; if the object is modified, the change is reflected across all variables referencing it.

```python
a = [1, 2, 3]       # Creates a list object
b = a
c = b
b[1] = 5
print(a, b, c)      # Prints [1, 5, 3] three times
```

For immutable values (like integers or strings), assigning a new value to a variable does not modify the original object; instead, the variable is rebound to point to a new object.

```python
x = "a string"
x = 5       # Rebinds x
del x       # Deletes the variable binding
```

## Strings and Formatted Literals (f-strings)

Strings can be enclosed in single (`'`), double (`"`), or triple (`"""` or `'''`) quotes.

### Modern f-strings (Formated String Literals)

f-strings provide a readable and concise way to format strings.

```python
name = "Alice"
age = 30

# Standard f-string
print(f"Name: {name}, Age: {age}")  # Output: Name: Alice, Age: 30

# 1. Debugging shorthand (Python 3.8+)
print(f"{name=}, {age=}")           # Output: name='Alice', age=30

# 2. Modern 3.12+ f-string updates:
# - Nested quotes: You can reuse the same quote characters inside the expression
# - Backslashes: Allowed directly inside expressions
# - Newlines: Allowed inside expressions
users = ["Alice", "Bob"]
print(f"First user: {users[0].upper() if len(users) > 0 else 'none'}")
print(f"Uppercase users: {', '.join([u.upper() for u in users])}")
```

## Numbers

- **Integers**: Arbitrary precision.
- **Floats**: Maximum 64-bit precision.
- **Booleans**: `True` (1) or `False` (0).

## The "None" Value

`None` is a special constant representing the absence of a value. It is a singleton.

## Truthiness and Falsy Values

Most objects can be evaluated in boolean contexts (like `if` statements). By default, empty collections (`[]`, `{}`, `()`, `""`), numeric zeros (`0`, `0.0`), and `None` are falsy. Other objects are truthy.

### Custom Class Truthiness
You can control the truthiness of custom classes by defining `__bool__()` or `__len__()` magic methods.

```python
class Account:
    def __init__(self, balance):
        self.balance = balance

    def __bool__(self):
        return self.balance > 0

acc = Account(100)
if acc:
    print("Account is active (balance > 0)")
```

## Security Warning: The Danger of `eval()` and `exec()`

> [!CAUTION]
> **Avoid using `eval()` or `exec()` to dynamically run or calculate expressions from user inputs.**
> If an application calls `eval(user_input)`, an attacker can pass a malicious string to execute shell commands, read/write local files, or shut down the application.

* **Bad (Command Injection/RCE)**:
  ```python
  # User inputs: "__import__('os').system('rm -rf /')"
  result = eval(user_input)
  ```
* **Good (Safe Parsing)**:
  Use safe standard libraries like `ast.literal_eval()` (which only parses basic literals/structures) or parse values explicitly using safe functions (e.g. `int()`).
  ```python
  import ast
  # Safely parse a list or dict literal from a string
  safe_data = ast.literal_eval("[1, 2, 3]")
  ```

## Style Conventions (PEP 8)

- Use `snake_case` for variables, functions, and files.
- Use `PascalCase` for classes.
- Use 4 spaces per indentation level.
