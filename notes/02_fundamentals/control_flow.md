---
title: Control Flow
tags: [fundamentals, loops, conditionals, patterns]
status: complete
source: The Quick Python Book, Ch. 8
last_updated: 2026-07-10
---

# Control Flow

## The `while` Loop

```python
while condition:
    body         # Loop body statements
else:            # Optional, executed when condition becomes False
    post-code    # Post-loop statements (not executed if break is used)
```

`condition` is a boolean expression. As long as it evaluates to `True`, the `body` is executed. Once it evaluates to `False`, the optional `else` block runs.

- `break`: Immediately exits the loop, skipping the `else` block.
- `continue`: Skips the rest of the current iteration and goes back to the condition evaluation.

## The `if-elif-else` Statement

```python
if condition1:
    body1
elif condition2:
    pass         # Place-holder when no action is needed
else:
    body3
```

When an empty block is syntactically required but no action is needed, use the `pass` statement.

### Switch Case Alternatives
Python does not have a traditional `switch` statement (prior to Python 3.10 match-case). Alternatives include using `if-elif-else` chains or a dictionary of functions:

```python
def a_func():
    # Execute code for 'a'
    pass

def b_func():
    # Execute code for 'b'
    pass

def c_func():
    # Execute code for 'c'
    pass

dicc_fc = {
    'a': a_func,
    'b': b_func,
    'c': c_func
}

x = 'a'
dicc_fc[x]()  # Executes the function mapped to the key 'a'
```

*See companion code: [control_flow.py](examples/08_control_flow.py)*

## The `for` Loop

Iterates over any iterable sequence (such as lists, tuples, or strings).

```python
for item in sequence:
    body
else:                     # Optional, executed after iteration finishes
    post-code
```

The `break` and `continue` statements work inside `for` loops in the same way they do in `while` loops.

### The `range` Function

Generates a sequence of integers:

```python
range(n)                  # 0, 1, 2 ... n-1
range(start, stop, step)  # Generates integers from start up to (but excluding) stop by step
```

Iterating through a list using index-based lookup:

```python
x = [1, -8, 2, -3, 9, 4]
for n in range(len(x)):
    if x[n] > 0:
        print("Positive number at index:", n)
```

*See companion code: [control_flow.py](examples/08_control_flow.py)*

`range` returns a generator-like object that yields numbers on demand instead of storing the entire sequence in memory. This is highly efficient for large ranges.

For decreasing sequences, use a negative step value:

```python
list(range(8, 3, -2))   # Returns [8, 6, 4]
```

### Tuple Unpacking

A clean way to unpack sequence values directly inside a loop definition:

```python
pairs = [(1, 2), (3, 4), (5, 6)]
total = 0
for x, y in pairs:
    total += x * y
```

### The `enumerate` Function

Combines tuple unpacking with index tracking to iterate over index and value simultaneously. `enumerate(sequence)` yields `(index, item)` pairs.

```python
x = [1, -8, 2, -3, 9, 4]
for i, v in enumerate(x):
    if v > 0:
        print(f"Positive number at index: {i}")
```

*See companion code: [control_flow.py](examples/08_control_flow.py)*

Using `enumerate` is generally cleaner and more pythonic than iterating with `range(len(x))`.

### The `zip` Function

Combines elements from two or more iterables into tuples, stopping when the shortest iterable is exhausted.

```python
x = [1, 2, 3, 4]
y = ["a", "b", "c"]
z = zip(x, y)
list(z)  # Returns [(1, 'a'), (2, 'b'), (3, 'c')]
```

*See companion code: [loops_if.py](examples/08_loops_if.py)*

## List and Dictionary Comprehensions

Syntactic shortcuts for creating new lists or dictionaries from existing sequences using an inline loop:

```python
new_list = [expression for variable in old_sequence if condition]
new_dict = {key_expression: value_expression for variable in old_sequence if condition}

x = [1, 2, 3, 4]
squares_list = [item * item for item in x if item > 2]  # List comprehension
squares_dict = {item: item * item for item in x if item > 2}  # Dictionary comprehension
```

*See companion code: [control_flow.py](examples/08_control_flow.py)*

### Generator Expressions

A generator expression is written similarly to list comprehensions but uses parentheses instead of brackets. It returns an iterator rather than a fully instantiated collection in memory.

- **Advantage:** Low memory usage because elements are generated on demand.

```python
x = [1, 2, 3, 4]
squared_generator = (item * item for item in x)    # Creates a generator object
for val in squared_generator:
    print(val)
```

*See companion code: [comprehensions.py](examples/08_comprehensions.py)*

## Statements, Blocks, and Indentation

In rare cases, multiple statements can be placed on a single line separated by semicolons:

```python
x = 1; y = 2; z = 3
if x > 0: y = 1; z = 10
else: y = -1
print(x, y, z)      # Output: 1 1 10
```

However, it is highly recommended to follow PEP 8 standard formatting and use 4 spaces per indentation level (avoiding tab characters).

## Boolean Values and Expressions

Most Python objects can be evaluated directly in conditional expressions to determine if they are truthy or falsy.

| Data Type | Falsy Value | Truthy Value |
|---|---|---|
| Numbers | `0`, `0.0` | Any non-zero value |
| Strings | `""` | Any non-empty string |
| Lists | `[]` | Any non-empty list |
| Dictionaries | `{}` | Any non-empty dictionary |
| Sets/Tuples | `()` | Any non-empty set/tuple |
| None | `None` | Never |

In general, objects are evaluated as `False` if they are zero or empty.

### Operators and Comparisons
- **Comparison operators:** `<`, `<=`, `>`, `>=`, `==`, `!=`
- **Membership operators:** `in`, `not in`
- **Identity operators:** `is`, `is not`
- **Logical operators:** `and`, `or`, `not`

Logical `and` and `or` perform short-circuit evaluation:
- `and` returns the first falsy object evaluated, or the last object if all are truthy.
- `or` returns the first truthy object evaluated, or the last object if all are falsy.

Comparison:
- `==` and `!=` compare the **value/content** of operands.
- `is` and `is not` compare the **identity** (memory reference) of operands.

## Example: Word Count Utility

A script that reads a text file and prints its lines, words, and characters (similar to the UNIX `wc` tool):

```python
#!/usr/bin/env python3
"""Reads a file and returns counts for lines, words, and characters."""

line_count, word_count, char_count = 0, 0, 0
with open('word_count.tst') as file:
    for line in file:
        line_count += 1
        words = line.split()
        word_count += len(words)
        char_count += len(line.strip(",.\t\n "))

print(f"Lines: {line_count}, Words: {word_count}, Characters: {char_count}")
```

*See companion code: [word_count.py](examples/08_word_count.py)*
