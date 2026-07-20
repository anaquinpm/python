---
title: Exception Handling
tags: [fundamentals, error-handling, exceptions, try-except]
status: complete
source: General Reference
last_updated: 2026-07-20
---

# Exception Handling

Python uses exceptions to manage errors and exceptional events during program execution. Proper exception handling ensures that programs are robust, fail gracefully, and do not leak sensitive information.

## Basic Syntax

The `try`, `except`, `else`, and `finally` blocks form the core of exception handling.

```python
try:
    # Code that might raise an exception
    with open("data.txt", "r") as file:
        content = file.read()
    value = int(content.strip())
    result = 100 / value
except FileNotFoundError as e:
    # Handle specific file missing error
    print(f"File not found: {e}")
except ValueError as e:
    # Handle parsing error
    print(f"Invalid integer format: {e}")
except ZeroDivisionError as e:
    # Handle division by zero
    print(f"Division error: {e}")
else:
    # Executed ONLY if no exceptions were raised in the try block
    print(f"Success! Result is: {result}")
finally:
    # ALWAYS executed, ideal for releasing resources
    print("Execution of block completed.")
```

## Raising Exceptions and Exception Chaining

You can manually raise exceptions using the `raise` statement. When catching an exception and raising a new one, use `raise ... from` to preserve the original traceback (exception chaining).

```python
def get_user_age(user_data):
    try:
        return int(user_data["age"])
    except KeyError as e:
        # Chain exceptions to preserve context
        raise ValueError("Age field is missing in user data") from e
    except ValueError as e:
        raise ValueError("Age must be a valid integer") from e
```

## Defining Custom Exceptions

To create custom exceptions, inherit from the built-in `Exception` class. Adding descriptive docstrings or attributes can help debug issues.

```python
class InsufficientFundsError(Exception):
    """Raised when an account balance is below the transaction amount."""
    def __init__(self, balance, amount):
        super().__init__(f"Attempted to withdraw ${amount} with balance of ${balance}")
        self.balance = balance
        self.amount = amount

# Usage
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount
```

## Best Practices and Security

### 1. Avoid Bare `except:` and generic `except Exception:`
A bare `except:` catches `BaseException`, which includes `SystemExit`, `KeyboardInterrupt`, and `GeneratorExit`. This makes it difficult to terminate the program.
* **Bad:**
  ```python
  try:
      do_something()
  except:
      pass  # Swallows all errors, including Ctrl+C
  ```
* **Good:**
  ```python
  try:
      do_something()
  except Exception as e:
      # Logs or handles general application errors, but allows system signals through
      logger.error(f"Error occurred: {e}")
  ```

### 2. Avoid Information Disclosure
When writing production systems, do not leak raw exception messages or stack traces to end users. Attackers can exploit details of paths, databases, or libraries.
* **Bad (in API handler):**
  ```python
  def get_user_data():
      try:
          execute_query()
      except Exception as e:
          # Might leak DB connection strings or paths
          return {"error": str(e)}, 500
  ```
* **Good:**
  ```python
  def get_user_data():
      try:
          execute_query()
      except Exception as e:
          logger.exception("Database query failed")  # Log full details internally
          return {"error": "An internal server error occurred."}, 500  # Generic response to user
  ```

### 3. Leverage Context Managers
Prefer context managers (`with` statement) over manual cleanup in `finally` blocks for managing resources like files, locks, and network sockets. It is cleaner and less error-prone.
