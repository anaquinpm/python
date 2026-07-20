# Stage 4: System Commands & Regular Expressions

## Related Study Material

Before you start, make sure to read:
* **[Standard Library](../../../notes/10_standard_library/standard_library.md)**: Details on utilizing core library utilities, including the `subprocess` module.
* **[Regular Expressions](../../../notes/13_regex/regular_expressions.md)**: Pattern matching, searching, and extracting text using the `re` module.

**Goal**: Execute the Linux `df -h` command via Python's `subprocess` module, capture the output, and parse disk utilization using the `re` (regex) module.

## 1. Using `subprocess`

Sometimes reading files isn't enough; we need to run system utilities. We will use `subprocess.run` to securely call `df`.

```python
import subprocess
import re

def get_disk_usage():
    """Runs df -h and parses the output for high disk utilization."""
    try:
        # Securely run the command as a list of arguments (avoids shell injection)
        result = subprocess.run(["df", "-h"], capture_output=True, text=True, check=True)
        return parse_df_output(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        return []
```

## 2. Using Regular Expressions (`re`)

Create a helper function to parse the textual output of `df` to extract the mount point and the usage percentage.

```python
def parse_df_output(output):
    alerts = []
    # Regex pattern to match lines like: /dev/sda1  50G  40G  10G  80% /
    # We capture the percentage and the mount point.
    pattern = re.compile(r'\s+(\d+)%\s+(/.+)?$')
    
    for line in output.split('\n'):
        match = pattern.search(line)
        if match:
            usage_pct = int(match.group(1))
            mount_point = match.group(2)
            
            # Simple threshold check
            if usage_pct > 80:
                alerts.append({"mount": mount_point, "usage_pct": usage_pct})
                
    return alerts
```

## 3. Integration

Add the disk check to your `__main__` block and test it via the container terminal!
