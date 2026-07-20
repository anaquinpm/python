# Stage 3: Functions, Dictionaries & Error Handling

## Related Study Material

Before you start, make sure to read:
* **[Functions](../../../notes/04_functions/functions.md)**: Declaring functions, arguments, and scoping.
* **[Dictionaries](../../../notes/03_data_structures/dictionaries.md)**: Storing keys and values.
* **[Exception Handling](../../../notes/08_error_handling/exceptions.md)**: Handling runtime issues using `try` / `except` blocks.

**Goal**: Refactor the script from Stage 2. Wrap reading logic into reusable functions, store the parsed metrics in dictionaries, and handle errors securely.

## 1. Refactor to Functions

Create functions that return data structures (like dictionaries) instead of just printing raw strings. 

```python
def get_cpu_load():
    """Reads CPU load average and returns a dictionary."""
    try:
        with open("/proc/loadavg", "r") as f:
            data = f.read().split()
            return {
                "1_min": float(data[0]),
                "5_min": float(data[1]),
                "15_min": float(data[2])
            }
    except FileNotFoundError:
        print("Error: /proc/loadavg not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
```

## 2. Parse Memory into a Dictionary

Create a similar function `get_memory_info()`. Instead of returning strings, extract the numerical values and store them:

```python
def get_memory_info():
    """Reads memory info and returns total and free memory in kB."""
    mem_data = {}
    try:
        with open("/proc/meminfo", "r") as f:
            for line in f:
                if line.startswith("MemTotal:"):
                    mem_data["total_kb"] = int(line.split()[1])
                elif line.startswith("MemFree:"):
                    mem_data["free_kb"] = int(line.split()[1])
        return mem_data
    except Exception as e:
        print(f"Error reading memory: {e}")
        return {}
```

## 3. The Main Block

Update your script to use the typical Python `__main__` guard:

```python
if __name__ == "__main__":
    print("CPU Load:", get_cpu_load())
    print("Memory Info:", get_memory_info())
```

Execute it inside your container:
```bash
python monitor.py
```
