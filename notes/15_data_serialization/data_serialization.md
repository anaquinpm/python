---
title: Data Serialization
tags: [serialization, json, csv, pickle, yaml, security]
status: complete
source: Official Python docs, json/csv/pickle modules
last_updated: 2026-07-20
---

# Data Serialization

Data serialization is the process of converting complex data structures or object states into a format that can be stored (in a file or memory buffer) or transmitted over a network link, and reconstructed later.

## JSON Serialization (`json`)

JSON (JavaScript Object Notation) is a lightweight, language-independent data-interchange format. The `json` module is safe for untrusted data as it only represents standard values (numbers, strings, booleans, nulls, arrays, objects).

```python
import json

data = {
    "name": "Alice",
    "roles": ["admin", "developer"],
    "active": True,
    "rating": 4.8
}

# 1. Serialize to string (dumps) and file (dump)
json_string = json.dumps(data, indent=2)
with open("user.json", "w") as file:
    json.dump(data, file)

# 2. Deserialize from string (loads) and file (load)
parsed_data = json.loads(json_string)
with open("user.json", "r") as file:
    loaded_data = json.load(file)
```

## CSV Serialization (`csv`)

For tabular data, the `csv` module provides `reader`/`writer` and `DictReader`/`DictWriter` (useful for mapping rows to dictionaries).

```python
import csv

# Writing structured dictionary data to CSV
rows = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"}
]

with open("users.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "role"])
    writer.writeheader()
    writer.writerows(rows)

# Reading from CSV
with open("users.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], "->", row["role"])
```

## Pickle Serialization (`pickle`)

The `pickle` module is used for serializing and deserializing *native* Python object structures. 

```python
import pickle

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

player = Player("Alice", 100)

# Serialize object
serialized_player = pickle.dumps(player)

# Deserialize object
loaded_player = pickle.loads(serialized_player)
print(loaded_player.name)  # Output: Alice
```

## Security Warning: Insecure Deserialization (`pickle` and `yaml`)

> [!CAUTION]
> **NEVER unpickle data received from an untrusted or unauthenticated source.** 
> The `pickle` module is not secure. A maliciously crafted pickle stream can execute arbitrary system commands during deserialization.

### The Pickle Exploit Vector
An attacker can customize the deserialization process using the `__reduce__` method, which returns a tuple containing a callable and arguments to execute upon load:

```python
import pickle
import os

# Malicious payload designed to execute command on load
class Exploit:
    def __reduce__(self):
        # Executes 'whoami' when deserialized
        return (os.system, ('whoami',))

malicious_data = pickle.dumps(Exploit())

# In a vulnerable app, loading this executes the system command:
# pickle.loads(malicious_data)
```

### Safe Serialization Alternatives
- For general data: Use `json` or `msgpack`.
- For configuration files (YAML): Always use `yaml.safe_load(stream)` instead of `yaml.load(stream)` if using PyYAML, as the latter can also instantiate arbitrary Python classes.
