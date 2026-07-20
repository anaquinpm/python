# Stage 2: Basic File I/O & Data Types

## Related Study Material

Before you start, make sure to read:
* **[Environment Setup](../../../notes/01_setup/environment.md)**: Basic syntax verification and execution.
* **[Fundamentals Basics](../../../notes/02_fundamentals/basics.md)**: Variables and basic data types.
* **[File I/O](../../../notes/06_io/files.md)**: File reading mechanisms using context managers (`with` statement).

**Goal**: Write a simple script to read Linux virtual files (`/proc/loadavg` and `/proc/meminfo`) sequentially and print basic metrics to the console.

## 1. Create `monitor.py`

In your IDE, create `monitor.py` in the `hands-on/resource-sentinel/` directory.

## 2. Read CPU Load

The file `/proc/loadavg` contains CPU load averages. Read it using the `with` statement:

```python
# monitor.py
print("--- CPU Load ---")
with open("/proc/loadavg", "r") as f:
    load_data = f.read()
    print("Raw Load Data:", load_data.strip())
```

## 3. Read Memory Info

The file `/proc/meminfo` contains memory statistics. Read the first few lines:

```python
print("\n--- Memory Info ---")
with open("/proc/meminfo", "r") as f:
    # Read the first line (MemTotal)
    mem_total = f.readline().strip()
    # Read the second line (MemFree)
    mem_free = f.readline().strip()
    
    print(mem_total)
    print(mem_free)
```

## 4. Run and Validate

Go to the terminal where your Docker container is running (from Stage 1) and execute:

```bash
python monitor.py
```

You should see the metrics from the Linux environment of the container.
