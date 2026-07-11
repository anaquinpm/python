---
title: Functions
tags: [fundamentals, functions, syntax, arguments, decorators, generators]
status: complete
source: The Quick Python Book, Ch. 9
last_updated: 2026-07-10
---

# Functions

*See companion code: [functions.py](examples/09_functions.py)*

## Basic Function Definition

```python
def name(parameter1, parameter2, ...):
    """Function docstring description (optional)"""
    body
```

```python
def factorial(n):
    """Returns the factorial of a given integer."""
    r = 1
    while n > 0:
        r *= n
        n -= 1
    return r          # Value returned by the function

print(factorial(int(input("Enter a number: "))))
```

The docstring describes what the function does and what parameters it accepts.

When a `return arg` statement is executed, the value `arg` is returned and control exits the function. If a function does not return an explicit value, it automatically returns `None`.

## Parameter and Argument Options

### Positional Parameters

Arguments are bound to parameters in the order they are passed to the function:

```python
def power(x, y):
    """Calculates x to the power of y."""
    r = 1
    while y > 0:
        r *= x
        y -= 1
    return r

print(power(3, 3))    # Returns 27
```

*See companion code: [functions.py](examples/09_functions.py)*

The number of arguments passed must match the number of parameters defined, unless default values are provided.

### Default Values

Parameters can be defined with default values, which are used if the argument is omitted in the call. Parameters with default values must be declared *after* any parameters without default values.

```python
def func(arg1, arg2, arg3=default3, arg4=default4):
    ...
```

```python
def power(x, y=2):
    """Calculates x to the power of y. Defaults to squaring the number (y=2)."""
    r = 1
    while y > 0:
        r *= x
        y -= 1
    return r

print(power(3))      # Returns 9 (uses default y=2)
print(power(3, 4))   # Returns 81
```

### Keyword Arguments (Named Arguments)

You can specify parameter names when calling a function. The order of arguments does not matter when using keywords.

```python
power(y=3, x=2)
```

Combining keyword arguments and default values is highly useful for functions with many parameters that have sensible defaults:

```python
def file_info(size=False, create_date=False, mod_date=False):
    # ...
    return info

info = file_info(size=True, mod_date=True)
```

### Variable Number of Arguments

#### Arbitrary Positional Arguments (`*args`)

Prefixed with a single asterisk `*`, extra positional arguments are captured as a tuple.

```python
def maximum(*numbers):
    """Determines the maximum value from an arbitrary list of numbers."""
    if len(numbers) == 0:
        return None
    
    max_num = numbers[0]
    for n in numbers[1:]:
        if n > max_num:
            max_num = n
    return max_num

print(maximum(6, 2, 3, -9, 24))  # Returns 24
```

*See companion code: [functions.py](examples/09_functions.py)*

#### Arbitrary Keyword Arguments (`**kwargs`)

Prefixed with a double asterisk `**`, extra keyword arguments are captured as a dictionary.

```python
def report_args(x, y, **others):
    print(f"x: {x}, y: {y}, keys in 'others': {list(others.keys())}")

report_args(3, y=2, foo=3, bar=4)
# Output: x: 3, y: 2, keys in 'others': ['foo', 'bar']
```

### Argument Ordering Rules

When mixing different argument types, they must appear in this order:
1. Positional arguments
2. Keyword arguments
3. Arbitrary positional arguments (`*args`)
4. Arbitrary keyword arguments (`**kwargs`)

## Mutable Objects as Arguments

Arguments are passed by object reference.
- For **immutable** types (strings, numbers, tuples), changes inside a function do not affect the caller.
- For **mutable** types (lists, dicts, class instances), changes inside the function will modify the object and be visible outside the function.

## Variable Scopes

- **Local Variables:** Defined inside a function; accessible only during function execution.
- **Nonlocal Variables:** Defined in an outer enclosing function scope, accessed via the `nonlocal` statement.
- **Global Variables:** Defined at the module level; accessed from inside functions via the `global` statement to allow binding modifications.

*See companion code: [Scope examples](examples/09_nonlocal.py)*

## First-Class Functions

In Python, functions are first-class objects. They can be assigned to variables, stored in collections, or passed to other functions.

```python
def f_to_kelvin(deg_f):
    return 273.15 + (deg_f - 32) * 5 / 9

def c_to_kelvin(deg_c):
    return 273.15 + deg_c

# Assign to a variable
abs_temp = f_to_kelvin
print(abs_temp(32))

abs_temp = c_to_kelvin
print(abs_temp(0))

# Store in a dictionary
conversion_map = {'FtoK': f_to_kelvin, 'CtoK': c_to_kelvin}
print(conversion_map['FtoK'](32))
```

## Lambda Expressions

Lambda expressions are small, anonymous, inline functions defined in a single line.

```python
lambda parameter1, parameter2: expression
```

The conversion map above can be rewritten using lambdas:

```python
temp = {
    'FtoK': lambda deg_f: 273.15 + (deg_f - 32) * 5 / 9,
    'CtoK': lambda deg_c: 273.15 + deg_c
}
print(temp['FtoK'](32))
```

## Generator Functions

Generators are special functions used to implement custom iterators. They use the `yield` statement to yield values one at a time. The local variables of the generator are preserved between successive calls.

```python
def count_to_four():
    x = 0
    while x < 4:
        print("in generator, x =", x)
        yield x
        x += 1

for i in count_to_four():
    print(i)
```

### `yield from`

Introduced in Python 3.3, `yield from` delegates part of the generator's operations to another sub-generator.

```python
def subgen(x):
    for i in range(x):
        yield i

def gen(y):
    yield from subgen(y)

for q in gen(6):
    print(q)
```

## Decorators

A decorator is a function that takes another function as an argument, extends or modifies its behavior, and returns a new function wrapper.

Use the `@decorator_name` syntax immediately preceding the target function definition.

```python
def decorate(func):
    print("Decorating", func.__name__)
    def wrapper_func(*args):
        print("Executing wrapper around", func.__name__)
        return func(*args)
    return wrapper_func

@decorate
def my_function(param):
    print(param)

my_function("hello")
```

*See companion code: [Decorator example](examples/09_decorator.py)*
