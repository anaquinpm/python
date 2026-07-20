---
title: Logging and Debugging
tags: [logging, debugging, pdb, breakpoint, traceback, security]
status: complete
source: Official Python docs, logging/pdb modules
last_updated: 2026-07-20
---

# Logging and Debugging

Debugging allows developers to inspect program state at runtime, while structured logging provides persistent visibility into application health and security events.

## Debugging with `breakpoint()` and `pdb`

Python 3.7+ includes the built-in `breakpoint()` function. It calls the active debugger (by default, Python's standard Interactive Source Debugger `pdb`).

```python
def process_payment(amount):
    discount = 0.1
    final_amount = amount - (amount * discount)
    
    # Drops into interactive shell during execution
    breakpoint() 
    
    return final_amount
```

### Common `pdb` Commands:
- `h` (help): Show available commands.
- `n` (next): Execute the next line of code.
- `s` (step): Step inside a function call.
- `c` (continue): Continue execution until the next breakpoint.
- `p variable` (print): Print the value of a variable.
- `q` (quit): Exit the debugger.

## The `traceback` Module

Use the `traceback` module to capture, format, and safely output call stacks.

```python
import traceback

try:
    1 / 0
except ZeroDivisionError:
    # Get formatted traceback string
    tb_string = traceback.format_exc()
    # Log the traceback string to a file or secure logging channel
```

## The `logging` Module

Avoid using `print()` for application logging. The `logging` module offers 5 severity levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) and configurable handlers (Console, Files, Syslog).

```python
import logging

# Basic configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(),  # Console
        logging.FileHandler("app.log")  # File
    ]
)

logger = logging.getLogger("payment_gateway")
logger.info("Initializing payment systems.")
logger.error("Failed to connect to merchant API.")
```

## Security and Best Practices

### 1. Prevent Log Injection
Log injection occurs when an application logs unsanitized user inputs. If an attacker inputs carriage returns (`\r\n`), they can forge log entries to hide their actions or mislead administrators.
* **Bad**:
  ```python
# Input from user: "success\r\n2026-07-20 [INFO] User admin logged in"
logger.info(f"User login attempt for: {user_input}")
  ```
* **Good**: Sanitize inputs by removing newline and carriage return characters before logging.
  ```python
clean_input = user_input.replace("\n", "").replace("\r", "")
logger.info(f"User login attempt for: {clean_input}")
  ```

### 2. Protect PII and Sensitive Data
Ensure your logging configuration does not record sensitive credentials, passwords, session tokens, or PII (Personally Identifiable Information like SSNs, credit card numbers). Implement filter classes to mask values.

```python
class SensitiveDataFilter(logging.Filter):
    def filter(self, record):
        # Clean sensitive keys from log messages
        if "password" in record.msg:
            record.msg = "[REDACTED MESSAGE DUE TO SENSITIVE DATA]"
        return True
```

### 3. Traceback Handling in Production
Never expose raw tracebacks (stack traces) to end users in web applications. Tracebacks expose library versions, directory paths, and source code details that help attackers find vulnerabilities. Log tracebacks internally and show users generic error codes.
