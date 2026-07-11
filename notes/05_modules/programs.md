---
title: Python Programs and Scripts
tags: [fundamentals, scripts, execution, arguments, command-line]
status: complete
source: The Quick Python Book, Ch. 11
last_updated: 2026-07-10
---

# Python Programs

## Making Executable Scripts in Unix

To run a Python script directly from the shell:

```bash
chmod +x script_name.py       # Grant execute permission to the script
which python3                 # Locate the path to the python3 executable
```

Once the path is known, add it as the first line of the script (shebang):

```python
#!/usr/bin/env python3
```

Then run it using:

```bash
./script_name.py args
```

## A Basic Script

```python
# script1.py
import sys

def main():
    print("This is our first script file.")
    print("Command line arguments received:", sys.argv)

main()
```

*See companion code: [Code examples](examples/script1.py)*

Run it in the command line:

```bash
./script1.py arg1 arg2
```

`sys.argv` is a **list** containing the script name at index 0, followed by the command-line arguments.

### Redirecting Input/Output

You can read standard input (`sys.stdin`) and write to standard output (`sys.stdout`) to allow input/output redirection:

```python
# replace.py
import sys

def main():
    contents = sys.stdin.read()   # Reads standard input
    # Replaces occurrences of arg1 with arg2 and writes to stdout
    sys.stdout.write(contents.replace(sys.argv[1], sys.argv[2]))

main()
```

*See companion code: [Code examples](examples/replace.py)*

Run using redirection operators:

```bash
./replace.py a A < infile > outfile
```

You can also use Unix pipes (`|`) to chain scripts:

```bash
./replace.py a A < infile | ./replace.py b B > outfile
```

### The `argparse` Module

`argparse` makes it easy to write user-friendly command-line interfaces with options, default values, and automatically generated help messages.

```python
# opts.py
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()                                             
    parser.add_argument("indent", type=int, help="indent for report")     # Positional argument
    parser.add_argument("input_file", help="read data from this file")    # Positional argument
    parser.add_argument("-f", "--file", dest="filename", help="write report to FILE", metavar="FILE") # Optional argument
    parser.add_argument("-x", "--xray", help="specify xray strength factor")                          # Optional argument
    parser.add_argument("-q", "--quiet", action="store_false", dest="verbose", default=True, help="don't print status messages to stdout")
    args = parser.parse_args()
    print("Arguments:", args)

main()
```

*See companion code: [Code examples](examples/opts.py)*

Test script execution:

```bash
./opts.py -x100 -q -f outfile 2 arg2      # Works
./opts.py -x100 -q -f outfile 2           # Raises an error due to missing arg2
```

### The `fileinput` Module

Useful for looping over lines from one or multiple input files.

```python
# script5.py
import fileinput

def main():
    for line in fileinput.input():           # If no args are passed, fileinput uses sys.argv[1:]
        if fileinput.isfirstline():          # Check if it's the first line of the current file
            print(f"<Start of file {fileinput.filename()}>")
        if not line.startswith('##'):        # Print non-commented lines
            print(line, end="")
    print(f"\nTotal lines read: {fileinput.filelineno()}")

main()
```

*See companion code: [Code examples](examples/script5.py)*

Run against multiple files:

```bash
./script5.py sole1.tst sole2.tst
```

- Useful UNIX System Administration Modules:
  - `grp`
  - `pwd`
  - `resource`
  - `syslog`
  - `stat`

## Programs and Modules

*See companion code: [Number-to-words example](examples/num2words.py)*

To write Python files that can be executed as standalone scripts *and* imported as reusable modules, use the `__name__` conditional check:

```python
if __name__ == '__main__':
    main()
else:
    # Module-specific initialization code if imported
    pass
```

When run directly, Python sets `__name__` to `'__main__'`. If imported, `__name__` is set to the name of the module file.

*See companion code: [Command line tester](examples/n2w.py)*

```bash
# Execute as a script
./n2w.py 199
./n2w.py --test < n2w.tst > n2w.txt

# Import as a module in the REPL
>>> import n2w
>>> n2w.num2words("1,234")
```

## Distributing Python Applications

- **Wheels**: The standard package format for Python. It facilitates easy installation and handles dependencies. Learn more at [Python Packaging User Guide](https://packaging.python.org).
- **Zipapp**: Packages a directory containing a `__main__.py` file into a single executable archive file.
- **Pex**: A third-party packaging tool (installable via `pip`) with advanced bundling and environment configuration features.
- **py2exe / PyInstaller / Freeze**: Package Python applications into standalone executables (e.g. for Windows/macOS/Linux) so they can run on systems without Python installed.
