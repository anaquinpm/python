#monitor.py
print("---- CPU Load ----")
with open("/proc/loadavg", "r") as f:
    load_data = f.read()
    print("Raw Load Data:", load_data.strip())

print("---- Memory Info ----")
with open("/proc/meminfo", "r") as f:
    mem_total = f.readline().strip()
    mem_free = f.readline().strip()

    print(mem_total)
    print(mem_free)