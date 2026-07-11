---
title: Python Basics
tags: [fundamentals, basics, syntax, variables, types]
status: complete
source: The Quick Python Book, Ch. 4
last_updated: 2026-07-10
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

Variables can point to any type of object (dynamic typing).

```python
x = "a string"
print(x)
x = 5
print(x)
del x       # Deletes the variable binding
```

Variable names are case-sensitive and can contain alphanumeric characters and underscores.

## Expressions

Python supports standard arithmetic expressions.

```python
x, y = 3, 4         # Multiple assignment
z = (x + y) / 2     # Standard division (returns float)
z = (x + y) // 2    # Floor division (returns truncated integer)
```

## Strings

Strings can be enclosed in either single quotes (`'`) or double quotes (`"`).

Special characters can be escaped using a backslash (`\`): `\n` (newline), `\t` (tab), `\"` (double quote), etc.

Triple quotes (`'''` or `"""`) allow multi-line strings without needing explicit escape characters:

```python
text = """This is a string
that can span multiple lines and contain 'quotes'
without needing to escape them."""
```

## Numbers

Python handles four types of numbers:
- **Integers**: Arbitrary precision (limited only by system resources).
- **Floats**: Maximum 64-bit precision, written as decimals or in scientific notation.
- **Complex Numbers**
- **Booleans**: `True` (1) or `False` (0).

```python
>>> 9 / 2
4.5
>>> 9 // 2      # Truncates division to return integer part
4
>>> int(2.3e2)  # Converts float from scientific notation to integer
230
>>> float(9 / 3)
3.0
```

### Built-in Numeric Functions
`abs`, `divmod`, `float`, `hex`, `int`, `max`, `min`, `oct`, `pow`, `round`

### Advanced Math Module
Import functions from the `math` module for more complex operations.

```python
from math import *      # Imports mathematical functions
```

Common functions: `acos`, `asin`, `atan`, `cos`, `ceil`, `exp`, `e`, `hypot`, `log`, `log10`, and others.

### Scientific/Numeric Computation
[NumPy](https://numpy.org) is a popular package used for implementing advanced mathematical operations, matrices, Fourier transforms, and more.

## The "None" Value

`None` is a special constant representing the absence of a value (empty placeholder).

If a function does not return a value, it returns `None` by default.

`None` is a singleton; all variables referencing `None` point to the exact same object.

## Getting User Input

```python
"""Example program to calculate the factorial of a user-supplied number"""
# The input() function returns a string by default. We convert it using int()
n = int(input("Enter a number to factorize: "))
r = 1
while n > 0:
    r *= n
    n -= 1
print(r)
```

## Style Conventions

Refer to [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) for community conventions:

- Use `snake_case` for functions, variables, and modules: `my_func`, `my_var`, `my_module`
- Use `PascalCase` for classes: `MyClass`
- Use `UPPER_CASE` for constants: `CONST_NAME`
