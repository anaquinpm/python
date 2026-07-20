---
title: Standard Library Overview
tags: [stdlib, os, sys, datetime, collections, math, pathlib, argparse]
status: complete
source: Official Python Tutorial Ch. 10-11
last_updated: 2026-07-20
---

# Standard Library Overview

The Python Standard Library provides a vast collection of built-in modules to handle common operations out-of-the-box. Leveraging these built-ins leads to more readable, standardized, and secure code.

## File System Operations (`pathlib` vs `os`)

Modern Python code should favor the object-oriented `pathlib` module over legacy string-based `os` or `os.path` functions. `pathlib` provides a cleaner API and reduces risks of path traversal vulnerabilities.

```python
from pathlib import Path

# Legacy way: os.path.join(base_dir, "subdir", "file.txt")
# Modern pathlib way:
base_path = Path("/workspace/data")
file_path = base_path / "subdir" / "file.txt"

print(file_path.name)       # Output: file.txt
print(file_path.suffix)     # Output: .txt
print(file_path.exists())   # Returns True or False

# Security check: Prevent Path Traversal (Directory Traversal)
# Ensure target path remains within the base directory
def is_safe_path(base_dir, target_path):
    try:
        base = Path(base_dir).resolve()
        target = Path(target_path).resolve()
        return base in target.parents or base == target
    except (ValueError, RuntimeError):
        return False
```

## Date and Time Management (`datetime`)

When working with datetimes, **always use timezone-aware objects** to avoid bugs caused by DST shifts or differing server local times.

```python
from datetime import datetime, timezone

# Bad: Timezone-naive datetime (assumes local time, prone to ambiguity)
naive_now = datetime.now()

# Good: Timezone-aware UTC datetime
utc_now = datetime.now(timezone.utc)
print(utc_now.isoformat())  # Output e.g., '2026-07-20T10:35:00+00:00'
```

## System Interfaces (`sys` and `argparse`)

For reading command-line arguments, do not parse raw `sys.argv` arrays manually. Use `argparse` to handle validation, default values, and automatically generate help menus.

```python
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Process database backup.")
    parser.add_argument("--host", required=True, help="Database host address")
    parser.add_argument("--port", type=int, default=5432, help="Database port")
    return parser.parse_args()
```

## Specialized Containers (`collections`)

The `collections` module provides alternative high-performance container data types.

```python
from collections import Counter, defaultdict, deque

# 1. Counter: Count occurrences of elements
items = ["apple", "banana", "apple", "orange", "banana", "banana"]
counts = Counter(items)
print(counts["banana"])  # Output: 3

# 2. defaultdict: Dict that provides a default value for missing keys
# Avoids KeyError and manual checks
user_groups = defaultdict(list)
user_groups["admin"].append("Alice")
user_groups["staff"].append("Bob")

# 3. deque: Double-ended queue with fast O(1) appends and pops on both ends
queue = deque(["task1", "task2"])
queue.append("task3")
current = queue.popleft()  # Output: 'task1'
```

## Mathematics (`math`)

For floating-point and mathematical operations, use the built-in `math` module instead of manual implementations.

```python
import math

print(math.isclose(0.1 + 0.2, 0.3))  # Output: True (Safe float comparison)
print(math.ceil(4.2))                # Output: 5
```
