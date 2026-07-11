---
title: Strings
tags: [fundamentals, data-structures, string, encoding]
status: complete
source: The Quick Python Book, Ch. 6
last_updated: 2026-07-10
---

# Strings

*See companion code: [strings.py](examples/06_strings.py)*

## Strings as Sequences of Characters

You can extract characters or substrings from a string using indexing or slice notation.

```python
x = "Hello\n"
x[0]          # Returns "H"
x[:-1]        # Returns "Hello" -> Useful for stripping newline characters when reading files
x[1:-1]       # Returns "ell"
len(x)        # Returns 6
```

While Python provides specialized methods for string manipulation, strings can be sliced and indexed just like any other sequence.

The primary difference between a list and a string is that strings are **immutable** (cannot be modified in place).

```python
x = "Hello\n"
x = x[:-1]        # Because strings are immutable, we rebind the variable to a new string object
```

## Basic String Operations

```python
# Concatenation
x = "Hello " + "world"    # Returns "Hello world"

# Multiplication (repetition)
4 * "x"                 # Returns "xxxx"
```

## Special Characters and Escape Sequences

Special characters are represented using escape sequences starting with a backslash (`\`).

### Basic Escape Sequences

| Sequence | Representation |
|---|---|
| `\'` | Single quote |
| `\"` | Double quote |
| `\a` | Bell character (triggers a system beep) |
| `\b` | Backspace |
| `\\` | Backslash |
| `\n` | Newline |
| `\t` | Horizontal Tab |
| `\v` | Vertical Tab |

### Numeric and Unicode Escape Sequences

Any ASCII character can be represented in octal or hexadecimal base:

```python
print("\153")   # Octal representation -> "k"
print("\x6B")   # Hexadecimal representation -> "k"
```

In Python 3, all strings are Unicode, so characters can be escaped using their Unicode name or hexadecimal code:

```python
x = '\N{LATIN SMALL LETTER A}'    # Unicode name -> "a"
print('\u00E1')                   # Hexadecimal code -> "á"
```

### Representation vs Print Output

When using the interactive Python REPL:
- Evaluating a string variable directly displays its internal representation, including escape sequences.
- Using `print()` resolves the escape sequences into their visual representation (e.g., executing a newline).

```python
>>> x = "Hello world\n"
>>> x
'Hello world\n'
>>> print(x)
Hello world
(followed by a newline)
```

## String Methods

The built-in `str` class provides numerous methods. Because strings are immutable, these methods always return a new string object rather than modifying the original.

### Split and Join

`split` and `join` perform inverse operations:
- `split()` splits a string into a list of substrings based on a delimiter. By default, it splits on whitespace.
- `join()` takes an iterable of strings and joins them into a single string with the caller string as the delimiter.

> [!TIP]
> While the `+` operator is useful for joining a few strings, using `.join()` is much more efficient when concatenating collections of strings, as it avoids creating intermediate string objects in memory.

```python
"-".join(["join", "places", "dashes", "between", "words"])
# Returns "join-places-dashes-between-words"

words.split("-")           # Splits using "-" as the delimiter
words.split(None, 2)       # Splits on whitespace, creating at most 3 groups (maxsplit=2)
```

#### Example: Replacing Spaces with Dashes

```python
x = "Replace the spaces in this text with dashes"
"-".join(x.split())
```

### Strings to Numbers

Convert strings to numeric values using `int()` and `float()`. `int()` accepts an optional second argument specifying the number base:

```python
float('123.456')    # Returns 123.456
int('123')          # Returns 123 (base 10)
int('1000', 8)      # Returns 512 (base 8/octal)
int('1000', 2)      # Returns 8 (base 2/binary)
int('ff', 16)       # Returns 255 (base 16/hexadecimal)
```

### Whitespace

The characters considered whitespace can vary by operating system.

```python
import string
string.whitespace		# Returns characters considered whitespace on the current OS
```

Methods to strip leading/trailing whitespace:
- `strip()`: Removes leading and trailing whitespace.
- `lstrip()`: Removes leading whitespace.
- `rstrip()`: Removes trailing whitespace.

```python
x = "\t     Hello, World \n\r"
x.strip()               # Returns "Hello, World"

y = "www.world.com"
y.strip("w.")           # Returns "world.com" (removes any characters in the passed string)
```

## String Searching

`find()` searches for a substring inside a string and returns the index of its first occurrence, or `-1` if not found.

```python
# string.find(substring[, start][, end])
x = "chicken"
x.find("ck")      # Returns 3
x.count("ck")     # Returns 1 (number of occurrences)
x.find("c", 2)    # Returns 3 (starts searching from index 2)
```

Other search methods include:
- `rfind()`: Searches from right to left.
- `index()` / `rindex()`: Similar to `find`/`rfind`, but raises a `ValueError` instead of returning `-1` if the substring is not found.
- `startswith(prefix)` / `endswith(suffix)`: Returns a boolean. Can take a tuple of strings as an argument.

```python
x = "chicken"
x.startswith("ch")      # Returns True
x.endswith("en")        # Returns True
x.endswith(("en", "n")) # Returns True (returns True if any element in the tuple matches)
```

### Modifying Strings

```python
x = "chicken"
x.replace("ck", "y")     # Returns "chiyen"

# Using translation tables
x = "( -A ![number])"
table = x.maketrans("-!", "*^")      # Maps '-' to '*' and '!' to '^'
x.translate(table)                  # Returns "( *A ^![number])"
```

Common casing and formatting methods:
`lower()`, `upper()`, `capitalize()`, `title()`, `expandtabs()`, `zfill()`, `rjust()`, `ljust()`

### Modifying via List Manipulation

You can convert a string to a list of characters, modify it, and join it back.

```python
x = "Modifying data types"
temp_list = list(x)
# ... perform operations on temp_list ...
paragraph = "".join(temp_list[9:])
```

Note: This approach is not optimal for large strings due to the overhead of object instantiation.

### Object String Representations

Use `repr()` to obtain a string representation of an object.

```python
x = ['hello', 'world']
'object: ' + repr(x)           # Returns "object: ['hello', 'world']"
```

## String Formatting (`format`)

```python
# Positional and keyword formatting
"Steak is the {0} of the {1}".format("food", "Gods")
"The {food} is the food of the {user[0]}".format(food="steak", user=["Gods", "men"])

# Format specifiers
"The {0:10} is the food of the Gods".format("Steak")        # Field width of 10
"The {food:{width}} is the food of the Gods".format(food="Steak", width=10)

# Custom alignment and padding
"{0:&>10} is the food of the Gods".format("Steak")         # Align right, padded with '&'
```

## Formatted String Literals (f-strings)

f-strings evaluate expressions directly inside a string literal. They have less performance overhead than the `.format()` method.

```python
pi = 3.1415
message = f"pi is {pi:{10}.{3}}"    # Width of 10, precision of 3 digits
print(message)                      # Output: "pi is       3.14"
```

## Bytes Objects

A bytes object is a sequence of integers in the range 0-255, useful for binary data manipulation.

```python
unicode_char = "\N{LATIN SMALL LETTER A WITH ACUTE}"    # Unicode string: "á"
xb = unicode_char.encode()       # Encodes unicode string to bytes (UTF-8 by default)
xb.decode()                      # Decodes bytes object back to a string
```
