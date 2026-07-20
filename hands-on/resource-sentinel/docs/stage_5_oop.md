# Stage 5: Object-Oriented Design & Modules

## Related Study Material

Before you start, make sure to read:
* **[Object-Oriented Programming](../../../notes/07_oop/oop.md)**: Declaring classes, constructors, methods, and instances.
* **[Modules and Packages](../../../notes/05_modules/modules_and_scoping.md)**: Restructuring scripts into multi-file projects, imports, and scoping namespace.

**Goal**: Restructure the flat script. Create a `Monitor` class and divide logic into multiple files to simulate a real-world application structure.

## 1. Directory Structure

Split your single `monitor.py` script into a modular package layout:

```text
hands-on/resource-sentinel/
├── docker-compose.yml
├── main.py
└── sentinel/
    ├── __init__.py
    ├── cpu.py
    ├── memory.py
    └── disk.py
```

## 2. Move Logic into Modules

- Move `get_cpu_load()` to `sentinel/cpu.py`.
- Move `get_memory_info()` to `sentinel/memory.py`.
- Move `get_disk_usage()` to `sentinel/disk.py`.

## 3. Create a Controller Class

In `main.py`, create a class that orchestrates these modules. This encapsulates state (like thresholds or configuration) and abstracts the logic.

```python
# main.py
from sentinel import cpu, memory, disk

class SystemMonitor:
    def __init__(self, disk_alert_threshold=80):
        self.disk_alert_threshold = disk_alert_threshold

    def run_checks(self):
        print("Starting System Checks...")
        
        load = cpu.get_cpu_load()
        print(f"CPU Load: {load}")
        
        mem = memory.get_memory_info()
        print(f"Memory: {mem}")
        
        disk_usage = disk.get_disk_usage() # You may need to adapt disk.py to accept a threshold
        print(f"Disk Alerts: {disk_usage}")

if __name__ == "__main__":
    monitor = SystemMonitor(disk_alert_threshold=85)
    monitor.run_checks()
```

Run `python main.py` inside the Docker container to verify the module imports work correctly across the volume mount.
