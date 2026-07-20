---
title: Filesystem Manipulation
tags: [fundamentals, io, filesystem, path, os, pathlib]
status: complete
source: The Quick Python Book, Ch. 12
last_updated: 2026-07-10
---

# Using the Filesystem

## Pathnames

A path specifies the location of a directory or file. Python provides filesystem access modules like `os`, `os.path`, and the newer, object-oriented `pathlib`.

Python abstracts away operating system-specific differences (such as `/` on Unix vs `\` on Windows) so that your scripts remain portable across filesystems.

Path types:
- **Absolute Paths**: The full path from the filesystem root. Example: `/home/user/dev/script.py`
- **Relative Paths**: A path relative to a specific directory (usually the current working directory). Example: `dev/script.py`

```python
import os
print(os.getcwd())       # Returns the current working directory (CWD)
```

| Path | Symbol | Portable Representation |
|---|---|---|
| Current Directory | `.` | `os.curdir` |
| Parent Directory | `..` | `os.pardir` |

### File and Path Operations (`os.path`)

```python
import os

os.chdir("folder_name")     # Change the current working directory
print(os.listdir(os.curdir)) # Returns a list of filenames and directories in CWD

# Joining and splitting paths
joined = os.path.join('some', 'directory', 'file.txt')
print(os.path.split(joined))      # Returns a tuple: ('some/directory', 'file.txt')
print(os.path.basename(joined))   # Returns 'file.txt'
print(os.path.dirname(joined))    # Returns 'some/directory'
print(os.path.splitext(joined))   # Returns ('some/directory/file', '.txt')

# Expand environment variables
print(os.path.expandvars('$USER')) # Returns the environment variable value
```

Check the operating system name via `os.name` to write OS-specific logic:

```python
import os

if os.name == 'posix':         # Unix/Linux/macOS
    root_dir = "/"
elif os.name == 'nt':          # Windows
    root_dir = "C:\\"
else:
    root_dir = None
    print("Unknown operating system")
```

### The `pathlib` Module

`pathlib` offers an object-oriented approach to path manipulation using `Path` objects.

```python
from pathlib import Path

cur_path = Path()
print(cur_path.cwd())              # Returns a Path object representing CWD

# Joining paths using joinpath or the / operator
joined_path = cur_path.joinpath('bin', 'utils', 'disktools')
# Alternative: joined_path = cur_path / 'bin' / 'utils' / 'disktools'

a_path = Path('some', 'directory', 'file.txt')
print(a_path.name)                 # Output: "file.txt"
print(a_path.parent)               # Output: "some/directory"
print(a_path.suffix)               # Output: ".txt"
```

## Security: Preventing Directory Traversal

When taking user input to read or write a file, an attacker can input parent directory references (like `../../etc/passwd`) to escape the target directory. 

Always resolve paths fully using `.resolve()` and verify that the target path begins with the base directory path.

```python
from pathlib import Path

BASE_DIR = Path("/workspace/data").resolve()

def save_user_file(filename, content):
    # Construct target path
    target = (BASE_DIR / filename).resolve()
    
    # Check if base directory is a parent of the target path
    if BASE_DIR in target.parents or BASE_DIR == target:
        with open(target, "w") as file:
            file.write(content)
    else:
        raise PermissionError("Access denied: Path traversal attempt blocked.")
```

