---
title: Object-Oriented Programming (OOP)
tags: [fundamentals, oop, classes, properties, encapsulation]
status: complete
source: General Reference
last_updated: 2026-07-10
---

# Object-Oriented Programming (OOP)

Object-oriented Programming (OOP) is a programming paradigm that allows modeling real-world elements as objects, making code easier to structure, extend, and reuse.

```python
class Car:      # Define a class
    pass

car = Car()     # Instantiate a Car object
```

Variables belonging to an object are called **attributes**, representing its properties or state. Functions defined inside a class are called **methods**, representing its behaviors.

## Constructor

The constructor method in Python is named `__init__`. It must accept `self` as its first parameter to refer to the specific object instance being created.

```python
class Elevator:
    def __init__(self, starting_floor):
        self.make = "The Elevator Company"
        self.floor = starting_floor

# Creating the object
elevator = Elevator(1)
print(elevator.make)   # Access attribute
print(elevator.floor)  # Access attribute
```

## Access Control and Encapsulation

Python does not support true private access control levels (like private or protected keywords). Instead, conventions are used:

- **Single Underscore (`_attribute`)**: A soft convention indicating that the attribute is internal/private. External code should avoid accessing or modifying it directly.
- **Double Underscore (`__attribute`)**: Triggers **name mangling**, making it harder (but still technically possible) to access from outside the class.

```python
class Square:
    def __init__(self):
        self._height = 2
        self._width = 2

    def set_side(self, new_side):
        self._height = new_side
        self._width = new_side

square = Square()
square._height = 3      # Soft warning ignored; attribute is still mutable directly
```

If we name the attribute starting with `__` (e.g., `__height`), attempting to access `square.__height` directly raises an `AttributeError`. However, Python internally renames the attribute to `_ClassName__attributeName`. Thus, you can still access it using:

```python
square._Square__height = 3  # Accessing a mangled attribute
```

## Properties (`@property` Decorator)

Properties allow defining methods that can be accessed like standard attributes, providing a clean way to implement getters, setters, and input validation.

```python
class Square:
    def __init__(self, w, h):
        self.height = h
        self.__width = w

    def set_side(self, new_side):
        self.__height = new_side
        self.__width = new_side

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, new_value):
        """Setter for height with validation and sanitization (Best Practice)."""
        if not isinstance(new_value, (int, float)):
            raise TypeError("Height must be a number")
        if new_value >= 0:
            self.__height = new_value
        else:
            raise ValueError("Value must be non-negative")
```

## Dataclasses (`@dataclass` Decorator)

Introduced in Python 3.7, the `dataclasses` module provides a decorator to automatically generate boilerplate methods (like `__init__`, `__repr__`, `__eq__`) for classes that primarily exist to store data.

```python
from dataclasses import dataclass

@dataclass
class User:
    username: str
    email: str
    active: bool = True

# Usage
user = User("alice", "alice@example.com")
print(user)  # Output: User(username='alice', email='alice@example.com', active=True)
```

## Generic Classes (Python 3.12+ Syntax)

Python 3.12 (PEP 695) introduced a new, clean syntax for writing generic classes and functions directly using square brackets, matching modern type-hinting standards.

```python
# A generic Box class that can hold any type T
class Box[T]:
    def __init__(self, content: T):
        self.content: T = content

    def get_content(self) -> T:
        return self.content

# Usage: Box holds an integer
int_box = Box[int](123)
print(int_box.get_content())
```

