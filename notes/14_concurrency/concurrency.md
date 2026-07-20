---
title: Concurrency
tags: [concurrency, threading, multiprocessing, asyncio, async, await]
status: complete
source: Official Python docs, threading, asyncio modules
last_updated: 2026-07-20
---

# Concurrency

Concurrency in Python refers to executing multiple tasks overlapping in time. Python provides three main models: Threading, Multiprocessing, and Asynchronous I/O (`asyncio`).

## Threading vs. Multiprocessing vs. Asyncio

| Model | Implementation | Execution Type | Best For | GIL Impact |
|---|---|---|---|---|
| **Threading** | OS threads | Preemptive multitasking | I/O-bound tasks | Blocked by GIL |
| **Multiprocessing** | OS processes | Parallel execution | CPU-bound tasks | Bypasses GIL |
| **Asyncio** | Single thread | Cooperative multitasking | Network I/O-bound tasks | Blocked by GIL (runs single-threaded) |

> [!NOTE]
> The **GIL (Global Interpreter Lock)** is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once in standard CPython.

## The `threading` Module

Use threads for tasks that spend time waiting for external events (e.g. disk read/write, API responses). Use `threading.Lock` to prevent race conditions on shared data.

```python
import threading
import time

counter = 0
counter_lock = threading.Lock()

def increment():
    global counter
    for _ in range(1000):
        # Acquire lock before modifying shared state
        with counter_lock:
            temp = counter
            time.sleep(0.0001)  # Simulate small delay
            counter = temp + 1

threads = []
for _ in range(2):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Final Counter:", counter)  # Expect exactly 2000
```

## The `multiprocessing` Module

For CPU-intensive tasks (e.g., image manipulation, heavy computations), bypass the GIL by using separate operating system processes, which utilize different CPU cores.

```python
from multiprocessing import Process, Pool
import os

def compute_square(n):
    return n * n

if __name__ == "__main__":
    # Using a Process Pool for batch computation
    numbers = [1, 2, 3, 4, 5]
    with Pool(processes=os.cpu_count()) as pool:
        results = pool.map(compute_square, numbers)
    print("Computed Squares:", results)  # Output: [1, 4, 9, 16, 25]
```

## The `asyncio` Module (Asynchronous I/O)

Asyncio uses a single-threaded event loop to execute cooperative coroutines. Code suspends execution when waiting for network I/O, allowing other tasks to run.

```python
import asyncio

async def fetch_data(task_id, delay):
    print(f"Task {task_id}: Started fetching...")
    await asyncio.sleep(delay)  # Non-blocking pause
    print(f"Task {task_id}: Done!")
    return f"Result {task_id}"

async def main():
    # Run multiple tasks concurrently
    results = await asyncio.gather(
        fetch_data(1, 2),
        fetch_data(2, 1),
        fetch_data(3, 1.5)
    )
    print("All tasks finished. Results:", results)

# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())
```

## Best Practices and Security

### 1. Avoid Blocking the Event Loop in Asyncio
Never run sync blocking calls (like `time.sleep()`, heavy database queries, or CPU calculations) directly in an async function. They halt the entire event loop.
* **Bad**: `time.sleep(5)` inside an `async def`.
* **Good**: Use `await asyncio.sleep(5)` or offload sync functions to an executor:
  ```python
  async def run_blocking_task():
      loop = asyncio.get_running_loop()
      result = await loop.run_in_executor(None, sync_blocking_function, args)
  ```

### 2. Thread Safety and Deadlocks
Always acquire locks in a consistent order to avoid deadlocks. Keep critical sections protected by locks as short and simple as possible.

### 3. IPC (Inter-Process Communication) Security
When using `multiprocessing`, prefer safe pipes and queues over raw shared memory. Never deserialize untrusted objects passing between processes.
