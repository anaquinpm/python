# Stage 6: Configuration & Structured Logging

## Related Study Material

Before you start, make sure to read:
* **[Data Serialization](../../../notes/15_data_serialization/data_serialization.md)**: Formatting configurations using standard protocols like JSON.
* **[Logging & Debugging](../../../notes/16_logging_debugging/logging_and_debugging.md)**: Setting up output streams, file handlers, formatting levels, and structured alerts.

**Goal**: Load settings from a `config.json` file and use Python's built-in `logging` module to output structured logs instead of using `print()`.

## 1. JSON Configuration

Create a `config.json` file in the project root:

```json
{
    "thresholds": {
        "disk_pct": 85,
        "load_1m": 4.0
    },
    "log_file": "sentinel.log"
}
```

In `main.py`, load this file using the `json` module:

```python
import json

with open("config.json", "r") as f:
    config = json.load(f)
```

## 2. Structured Logging

Replace `print()` statements with the `logging` module. This is critical for DevOps because logs can be easily ingested by tools like Datadog, ELK, or CloudWatch.

```python
import logging

# Configure the logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(config.get("log_file", "app.log")),
        logging.StreamHandler() # Also print to console
    ]
)

logger = logging.getLogger("ResourceSentinel")

# Use it in your class
logger.info("System Monitor Initialized")
logger.warning("Disk space running low!")
logger.error("Failed to read /proc/loadavg")
```

## 3. Run and Validate

Run `python main.py` inside your container. You should see standardized log output in your console, and a new `sentinel.log` file created in your workspace!

---
**Congratulations!** You've built a modular, configurable, structurally-logged systems monitor that is natively developed and executed within a Docker container.
