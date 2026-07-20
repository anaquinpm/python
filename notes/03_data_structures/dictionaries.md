---
title: Dictionaries
tags: [fundamentals, data-structures, dictionary, hash-map]
status: complete
source: The Quick Python Book, Ch. 7
last_updated: 2026-07-10
---

# Dictionaries

*See companion code: [dictionaries.py](examples/07_dictionaries.py)*

Dictionaries are associative arrays or maps implemented using hash tables.

- **Keys** can be any immutable, hashable Python object (integers, strings, etc.) and serve as lookups.
- **Values** can be any Python object.
- Since Python 3.7, dictionaries are **guaranteed to preserve insertion order** as part of the language specification.
  - If compatibility with older legacy Python engines is required or you need specialized reordering capabilities, `collections.OrderedDict` can still be used.

```python
y = {}
y["zero"] = 3.14    # Arbitrarily assign a new key-value pair
y[1] = 'Goodbye'
print(y[1] + ', Friend.')
y[2] = 2
print(y["zero"] * y[2])
```

*See companion code: [Names and ages example](examples/07_name.py)*

## Dictionary Operations

```python
spanish_to_english = {'rojo': 'red', 'verde': 'green', 'azul': 'blue'}
len(spanish_to_english)           # Returns the number of items (3)
list(spanish_to_english.keys())   # Returns a list of keys
list(spanish_to_english.values()) # Returns a list of values
list(spanish_to_english.items())  # Returns a list of key-value tuples
del spanish_to_english['azul']    # Deletes the key 'azul' and its value
```

> [!NOTE]
> Dictionary methods like `.keys()`, `.values()`, and `.items()` return dynamic **view objects**. These views reflect changes to the dictionary immediately. If you iterate over these views while modifying the dictionary, it may raise a `RuntimeError`. Convert them to a static `list()` to prevent this.

```python
'rojo' in spanish_to_english                                  # Check key existence (returns True/False)
print(spanish_to_english.get('azul', 'No translation'))       # Returns 'No translation' if key doesn't exist (defaults to None)
print(spanish_to_english.setdefault('azul', 'No translation')) # Returns key value if present, else sets the key to default and returns it
```

### Copying Dictionaries

```python
x = {0: 'zero', 1: 'one'}

# Shallow copy: Copies references to the values
y = x.copy()          

# Deep copy: Recursively copies all values
import copy
z = copy.deepcopy(x)  

# Merging dictionaries (Legacy vs Modern Python 3.9+)
h = {1: 'One', 2: 'Two'}

# 1. Legacy update (modifies in-place)
x.update(h)

# 2. Modern Union operator '|' (creates a new dictionary)
d1 = {'a': 1, 'b': 2}
d2 = {'b': 99, 'c': 4}
merged = d1 | d2      # merged is {'a': 1, 'b': 99, 'c': 4}

# 3. Modern Union update operator '|=' (updates in-place)
d1 |= d2              # d1 is now {'a': 1, 'b': 99, 'c': 4}
```

## Example: Counting Word Frequencies

```python
paragraph = "Testing how we use python to count words"
occurrences = {}
for word in paragraph.split():
    occurrences[word] = occurrences.get(word, 0) + 1

for word in occurrences:
    print(f"The word '{word}' occurred {occurrences[word]} times")
```

*See companion code: [Word counting example](examples/07_words.py)*

> [!TIP]
> Since counting elements is a very common task, Python provides the `collections.Counter` class specifically designed for this purpose.

## Keys Eligibility

Any **immutable** and **hashable** object can be used as a dictionary key.

| Python Type | Immutable | Hashable | Dictionary Key |
|---|---|---|---|
| int | Yes | Yes | Yes |
| float | Yes | Yes | Yes |
| boolean | Yes | Yes | Yes |
| complex | Yes | Yes | Yes |
| str | Yes | Yes | Yes |
| bytes | Yes | Yes | Yes |
| bytearray | No | No | No |
| list | No | No | No |
| tuple | Yes | Sometimes (if all elements are hashable) | Sometimes |
| set | No | No | No |
| frozenset | Yes | Yes | Yes |
| dict | No | No | No |

## Sparse Matrices

You can represent a grid or matrix as a nested list:

```python
matrix = [[3, 0, -2, 11], [0, 9, 0, 0], [0, 7, 0, 0], [0, 0, 0, -5]]
element = matrix[2][1]   # matrix[row][column] -> Returns 7
```

**Sparse Matrices** are matrices where most elements are zero. We can represent them efficiently using a dictionary with tuple indices as keys, storing only the non-zero elements:

```python
matrix = {(0, 0): 3, (0, 2): -2, (0, 3): 11, (1, 2): 9, (2, 2): 7, (3, 3): -5}

# Retrieve an element safely using get() to default to 0 for non-stored indices
element = matrix.get((row, col), 0)
```

For advanced matrix and numerical operations, refer to the `NumPy` package.

## Dictionaries as Caches (Memoization)

If a function performs an expensive calculation based on its inputs, a dictionary can be used as a cache to avoid redundant computation:

```python
calculation_cache = {}

def calculate(a, b, c):
    if (a, b, c) in calculation_cache:
        return calculation_cache[(a, b, c)]
    else:
        # Perform expensive calculation here
        result = a + b + c
        calculation_cache[(a, b, c)] = result
        return result
```
