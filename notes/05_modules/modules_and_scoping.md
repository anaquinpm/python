---
title: Modules and Scoping Rules
tags: [fundamentals, modules, scoping, namespaces]
status: complete
source: The Quick Python Book, Ch. 10
last_updated: 2026-07-10
---

# Modules and Scoping Rules

## What is a Module?

A module is a file containing Python code. It defines a set of related functions, classes, or variables. The name of the module file (excluding the `.py` extension) determines the module name.

Modules can be written in Python, compiled C code, or C++ objects. They help organize large codebases into manageable pieces.

```python
# mymath.py - Example module
pi = 3.14159

def area(r):
    """Returns the area of a circle with radius r."""
    global pi
    return pi * r ** 2
```

*See companion code: [Module code](examples/mymath.py)*

Using a module in a Python REPL or script:

```python
import mymath
print(mymath.area(3))
```

*See companion code: [Code examples](examples/10_modules_and_scoping.py)*

Prefixing the function name with the module name (e.g., `mymath.area`) is called **namespaces qualification**. It prevents naming collisions between functions defined in different modules.

If you want to import a specific attribute directly without qualification:

```python
from mymath import pi
print(pi)
# Note: other functions like area still require mymath.area() qualification
```

### Reloading Modules

When editing a module and testing it inside an active REPL session, Python does not automatically reload the changes. You can force a reload using `importlib.reload`:

```python
import mymath
import importlib
importlib.reload(mymath)
```

## The `import` Statement

The `import` statement supports three variations:

1. **Standard Import**: Imports the module namespace.
   ```python
   import modulename
   ```
2. **Selective Import**: Imports specific objects directly into the current namespace.
   ```python
   from modulename import name1, name2
   ```
3. **Wildcard Import**: Imports all public names from the module.
   ```python
   from modulename import *
   ```
   > [!WARNING]
   > Use wildcard imports (`from module import *`) with caution. They can pollute the namespace and overwrite existing names.

## Module Search Path

Python searches for modules in the directories listed in `sys.path`.

```python
import sys
print(sys.path)
```

`sys.path` is a list of directory paths that Python searches sequentially. The first match stops the search.

The first element in `sys.path` is usually an empty string `""`, which instructs Python to search the current directory first.

### Custom Module Paths

To ensure your custom modules are discoverable:

1. **System Directories**: Place files in Python's standard library directory. *Not recommended*, as these can be overwritten during upgrades.
2. **Local Directory**: Keep custom modules in the same directory as the executing script. Good for project-specific modules.
3. **Custom Directories via `.pth` files**: Create a `.pth` file containing absolute paths to your custom module directories and place it in the `site-packages` directory. This is the **most recommended approach** for global developer setups.

## Private Names in Modules

By default, executing `from module import *` imports all names except those starting with a leading underscore `_`. This serves as a convention for hiding internal helper functions or variables.

However, private names can still be accessed if imported explicitly or accessed using qualified naming:

```python
import mymodule
print(mymodule._private_variable)
```

## Scoping Rules and Namespaces

A **namespace** is a mapping from names (identifiers) to objects. Python uses namespaces to track variables and their active bindings.

When a block of code executes, Python resolves names in three hierarchical levels:
1. **Local** (inside the function/block)
2. **Global** (module-level)
3. **Built-in** (built-in functions like `len`, `range`, `ValueError`)

> [!CAUTION]
> Avoid shadowing built-in functions by using their names for custom variables (e.g., naming a list variable `list`). Doing so overrides the built-in reference in the current namespace.

`locals()` and `globals()` are built-in functions that return dictionaries containing the current local and global namespace bindings.

Use `del` to remove bindings from a namespace:

```python
x = 2
import math
from cmath import cos

del x, math, cos    # Deletes variables and references from the namespace
```

`dir()` without arguments returns names in the current local scope. When passed a module as an argument, it returns all names defined inside that module.

To get documentation on any built-in or module item:

```python
help(max)
print(max.__doc__)
```
