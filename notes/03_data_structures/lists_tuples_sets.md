---
title: Lists, Tuples, and Sets
tags: [fundamentals, data-structures, list, tuple, set]
status: complete
source: The Quick Python Book, Ch. 5
last_updated: 2026-07-10
---

# Lists, Tuples, and Sets

*See companion code: [lists_tuples_sets.py](examples/05_lists_tuples_sets.py)*

## Lists

A list is an ordered collection of objects.

```python
x = [1, "two", 3]           # Create a list
x = [4, [5, 6], "seven"]    # Elements can be any Python object
len(x)                      # Returns the number of elements in the list (3)
len(x[1])                   # Returns the number of elements in the object at index 1 (2)
```

You do not need to declare a variable before using it or specify its size; it expands or contracts dynamically as needed.

## List Indices

- Indices indicate the position of elements in a list.
- They are zero-indexed (starting from 0).
- Negative indices count elements from the end of the list, starting at `-1` for the last element.

| Position | first | second | third | fourth |
|---|---|---|---|---|
| Positive Indices | 0 | 1 | 2 | 3 |
| Negative Indices | -4 | -3 | -2 | -1 |

**Slicing** allows extracting or assigning a sublist in a single statement.

```python
x = ["one", "two", "three", "four"]
x[1:3]          # Returns elements from index 1 up to (but excluding) 3 -> ["two", "three"]
x[-3:-1]        # Returns ["two", "three"] using negative indexing
x[:3]           # Returns from index 0 up to 3 -> ["one", "two", "three"]
x[2:]           # Returns from index 2 to the end -> ["three", "four"]
x[:]            # Returns a shallow copy of the entire list
```

In slicing, omitting the first index default to `0`. Omitting the second index defaults to the end of the list.

## Modifying Lists

You can modify elements by index or replace entire slices.

```python
x = [1, 2, 3, 4]
x[2] = "three"           # Replaces the element at index 2 with the string "three"
```

Using slice notation, you can modify, add, or remove elements:

```python
x = [1, 2, 3, 4]
x[len(x):] = [5, 6, 7]  # Appends elements to the end of the list using slice notation
x.extend([5, 6, 7])     # Equivalent to the line above
x = [1, 2] + [4, 5]     # "+" concatenates two lists

x.append("item")        # Appends a single item to the list
x.append([2, 3, 4])     # Appends the list as a single nested element: [1, 2, 3, 4, [2, 3, 4]]
x[:0] = [-1, 0]         # Prepends elements to the start of the list

x.insert(3, "start")    # Inserts "start" at index 3. Supports negative indices
x[3:3] = ["start"]      # Inserts elements using slice notation (does not support negative indices)

del x[1:-1]             # "del" is the preferred method to remove items or slices
x[1:-1] = []            # Alternative slice-based removal (empties the range)

x.remove(6)             # Removes the first occurrence of the value 6. Raises ValueError if not found
                        # Tip: check existence with "in" first, or catch the exception

x.reverse()             # Reverses the list in place
```

## Sorting Lists

```python
x = [7, 2, 5, 1]
y = x[:]                # Create a copy of the list
y.sort()                # Sorts the list in place
```

All elements in a list must be of compatible types to be sorted, otherwise a `TypeError` will be raised.

To keep the original list unmodified, you can sort a copy or use the built-in `sorted()` function.

Elements are sorted in ascending lexicographical order by default.

### Custom Sorting

```python
def count_letters(word):
    return len(word)

my_list = ["Hello", "Python", "on", "progress"]
my_list.sort(key=count_letters)     # Sorts words by their length
```

*See companion code: [sorting example](examples/ordenando.py)*

Default sorting is generally faster than custom sorting. You can also reverse the sort direction using the `reverse=True` parameter:

```python
x = [1, 2, 3, 4, 5]
y = sorted(x, reverse=True)          # Returns a new list sorted in descending order; x remains unchanged
```

### The `in` Operator

Use `in` or `not in` to check for element existence in a sequence. Returns a boolean value.

```python
10 in [3, 5, 2, 10]     # True
4 not in [3, 5, 2, 10]  # True
```

### Initializing Lists with the `*` Operator

To allocate a fixed-size list and avoid the overhead of dynamic memory resizing (e.g., repeated `append` operations):

```python
x = [None] * 4      # Creates [None, None, None, None]
y = [1, 2] * 4      # Creates [1, 2, 1, 2, 1, 2, 1, 2]
```

### Minimum and Maximum Values

Returns the minimum or maximum element. Requires compatible, comparable types.

```python
min([4, 2, 6, 7])       # Returns 2
max([3, 7, "dog"])      # Raises TypeError (incompatible types)
```

### Searching by Index

`index(value)` returns the index of the first occurrence of the value. Raises `ValueError` if the value is not found.

```python
x = [1, 43, "dog", 39]
x.index(43)                 # Returns 1
x.index(2)                  # Raises ValueError
```

### Counting Occurrences

```python
x = [1, 2, 1, 2, 2, 4, 2, 6]
x.count(2)                  # Returns 4
```

## Nested Lists and Deep Copies

Two-dimensional arrays or matrices can be represented using nested lists.

```python
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
x[0][2]                                # Returns 3
x[1]                                   # Returns [4, 5, 6]
```

Since list elements can be references to mutable objects, modifying an inner list affects all references to it.

```python
x = ["one"]
y = [x, 2]          # [["one"], 2]
x[0] = 1            # Modifies the inner list
print(y)            # Output: [[1], 2]
```

When copying lists containing nested mutable structures, distinguish between shallow and deep copies:

```python
original = [["zero"], 1]

# Shallow copy: Copies references to the nested objects
shallow = original[:]           

# Deep copy: Recursively copies all objects
import copy
deep = copy.deepcopy(original)  
```

## Tuples

Tuples are ordered, **immutable** sequences of values. They are commonly used as keys in dictionaries.

```python
x = ('a', 'b', 'c')     # Declared using parentheses
# Built-in functions like len, count, min, and max are supported
x + x                   # Returns ('a', 'b', 'c', 'a', 'b', 'c')
x * 3                   # Returns ('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')
y = (1 + 2,)            # Single-element tuples require a trailing comma
```

Note: While the tuple itself is immutable (you cannot add, remove, or swap elements), if an element is a mutable object (like a list), that nested object can still be modified.

### Packing and Unpacking Tuples

```python
(a, b, c, d) = (1, 2, 3, 4)     # Unpacks values to variables
a, b, c, d = 1, 2, 3, 4         # Parentheses are optional
x, y = y, x                     # Value swap without a temporary variable

var = (1, 2, 3, 4)
a, b, *c = var                  # Unpacks remaining elements into a list: a=1, b=2, c=[3, 4]
a, *b, c = var                  # a=1, b=[2, 3], c=4
a, b, c, d, *e = var            # a=1, b=2, c=3, d=4, e=[]
```

### Conversions

```python
list(tuple_var)     # Converts a tuple to a list
tuple(list_var)     # Converts a list to a tuple
list("hello")       # Unpacks string characters into a list: ['h', 'e', 'l', 'l', 'o']
```

## Sets

A set is an unordered collection of unique elements. All elements must be **hashable and immutable** (integers, floats, strings, or tuples).

Sets behave similarly to dictionary keys without associated values.

```python
y = set()                       # the only way to create an empty set (the '{}' creates an empty dictionary)
x = set([1, 5, 4, 3, 5, 1])     # Create a set from a sequence
print(x)                        # Output: {1, 3, 4, 5} (duplicates removed)
x.add(6)                        # Adds an element
x.remove(1)                     # Removes an element
5 in x                          # Membership test (returns True)

y = set([1, 7, 5, 2])
x | y                           # Union -> {1, 2, 3, 4, 5, 7}
x & y                           # Intersection -> {1, 5}
x ^ y                           # Symmetric difference -> {2, 3, 4, 7}
```

Since standard sets are mutable, they are not hashable and cannot be elements of another set.

### Frozensets

Frozensets are immutable sets. Because they are immutable and hashable, they can be used as elements in other sets.

```python
z = frozenset(y)
```

*See companion code: [Lab example](examples/lab_temp.py)*
