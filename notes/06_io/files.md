---
title: File I/O
tags: [fundamentals, io, file, read, write, pathlib]
status: complete
source: The Quick Python Book, Ch. 13
last_updated: 2026-07-10
---

# Reading and Writing Files

```python
with open('archivo.txt', 'r') as file_object:
    line = file_object.readline()
```

The built-in `open()` function returns a **file object** which points to the target file. Input/Output (I/O) operations are executed on this object.

In the example above, the `with` statement acts as a **context manager**, ensuring that the file is automatically closed once block execution completes, even if exceptions occur.

## File Modes

The second argument of `open()` specifies the access mode:

| Mode | Description |
|---|---|
| `'r'` | Opens the file for reading (default). |
| `'w'` | Opens the file for writing. Overwrites or truncates the file if it exists. |
| `'a'` | Opens the file for appending. Writes new data at the end of the file. |
| `'rb'` | Opens the file for reading in binary mode (returns a bytes object instead of a string). |
| `'wb'` | Opens the file for writing in binary mode. |

> [!IMPORTANT]
> If you open a file using `open()` without a `with` statement, you must explicitly call `.close()` on the file object (e.g., `file_object.close()`) to free up system resources.

## Reading and Writing Operations

- `readline()`: Reads a single line from the file up to the newline character. Returns an empty string `""` when the end of file (EOF) is reached.
- `readlines()`: Reads all lines from the file and returns them as a list of strings. This loads the entire file contents into system memory.

An alternative, memory-efficient way to process a file line by line:

```python
file_obj = open("arch.txt", "r")
count = 0
for line in file_obj:
    count += 1
print("Lines counted:", count)
file_obj.close()
```

> [!TIP]
> Iterating directly over the file object (e.g., `for line in file_obj:`) is highly efficient. It uses buffering to read lines on demand without loading the entire file into memory at once.

- `write(string)`: Writes a string to the file.
- `writelines(sequence_of_strings)`: Writes a sequence (such as a list of strings) to the file.

*See companion code: [Read and write examples](examples/lines.py)*

### Binary File Operations

```python
input_file = open("binaryfile", "rb")
header = input_file.read(4)           # Read exactly 4 bytes
data = input_file.read()              # Read the remaining contents
input_file.close()
```

## File operations with `pathlib`

`pathlib.Path` objects provide high-level methods to read and write files directly without explicitly calling `open()` or `.close()`.

```python
from pathlib import Path

# Working with text files
p_text = Path('text.txt')
p_text.write_text('Some text content to write')
content = p_text.read_text()

# Working with binary files
p_binary = Path('binary_file.bin')
p_binary.write_bytes(b'Some binary bytes to write')
binary_data = p_binary.read_bytes()
```
