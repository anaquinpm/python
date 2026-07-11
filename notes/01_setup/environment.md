---
title: Environment Setup
tags: [setup, environment, venv]
status: complete
source: The Quick Python Book, Ch. 2
last_updated: 2026-07-10
---

# Environment

We can install **different** versions of Python on the same system.

Generally, Linux distributions come with a default Python installation.

```bash
python3 -V                    # View the Python version installed on the system
python2 -V
sudo apt install python3 python3-pip python3-venv     # On Debian/Ubuntu systems, install Python 3, pip, and venv
sudo apt install idle3        # Install the interactive IDLE shell
```

**`INFO`**: Refer to www.python.org for additional options to install on other operating systems.

We can use the interpreter in different ways:
- **Command Line**: Start the interactive REPL by typing `python3` in the shell prompt.
- **IDLE** (Integrated Development Environment): Provides basic GUI assistance; start by running `idle3` in the terminal.
- **Code Editor**: You can also write code directly using your preferred text editor/IDE.

## Hello World & Introspection

```python
print("Hello, world")       # In Python 3, print is a function, so parentheses are required
x = 2
help(x)                     # Function that provides documentation on keywords, modules, or topics
```

`help()` is powered by the `pydoc` library, which exposes documentation for Python libraries and user-defined code.

```python
dir()       # Function to inspect objects in a given namespace. Without arguments, it lists the global scope
globals()   # Returns a dictionary representing the current global symbol table
locals()    # Returns a dictionary representing the current local symbol table
```

These functions are useful for quickly listing methods, attributes, and data definitions in different *namespaces*.

## Creating a Virtual Environment (venv)

```bash
# Install the target Python version and its matching venv module
sudo apt install python[version] python[version]-venv
  # Example:
  sudo apt install python3.11{,-venv}

# Create a local virtual environment for project-specific dependencies
python3.9 -m venv <envs/myEnv>  # This runs the target python executable and creates the environment
  # Optional: include system packages in the environment
  python3.9 -m venv --system-site-packages <envs/myEnv>

# Note: Remember to add your virtual environment directory (e.g., envs/, .venv/, etc.) to .gitignore

# Activate the environment
source /envs/myEnv/bin/activate

# Deactivate the environment
deactivate
```
