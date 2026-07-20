---
title: Regular Expressions
tags: [regex, re, pattern-matching, text-processing, security]
status: complete
source: Official Python docs, re module
last_updated: 2026-07-20
---

# Regular Expressions

Regular expressions (regex) are powerful tools for pattern matching and text processing. Python's built-in `re` module implements Perl-style regular expressions.

## The `re` Module Functions

The `re` module offers multiple methods depending on whether you want to find the first match, all matches, or substitute text.

```python
import re

text = "Contact us at support@example.com or sales@example.org"

# 1. re.search: Find the FIRST match anywhere in the string
email_match = re.search(r"[\w.-]+@[\w.-]+\.\w+", text)
if email_match:
    print("Found email:", email_match.group())  # Output: support@example.com

# 2. re.findall: Find ALL matches as a list of strings
emails = re.findall(r"[\w.-]+@[\w.-]+\.\w+", text)
print(emails)  # Output: ['support@example.com', 'sales@example.org']

# 3. re.sub: Replace matches with a replacement string
masked_text = re.sub(r"[\w.-]+@[\w.-]+\.\w+", "[REDACTED]", text)
print(masked_text)  # Output: Contact us at [REDACTED] or [REDACTED]
```

## Compiling Regex and Using Flags

For patterns reused multiple times, compile them with `re.compile()` for better performance. You can also pass flags like `re.IGNORECASE` (or `re.I`) and `re.MULTILINE` (or `re.M`).

```python
import re

# Compile with Case-Insensitive flag
pattern = re.compile(r"python", re.IGNORECASE)

match = pattern.search("I love Python programming")
print(match.group())  # Output: Python
```

## Matching Groups and Named Groups

Parentheses `()` define matching groups. Named groups can be defined with `(?P<name>pattern)` for more readable parsers.

```python
import re

log_line = "2026-07-20 10:45:00 - ERROR - Database connection timeout"

pattern = re.compile(r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) - (?P<level>\w+) - (?P<msg>.*)")
match = pattern.match(log_line)

if match:
    print(match.group("level"))  # Output: ERROR
    print(match.group("msg"))    # Output: Database connection timeout
    # Access as dict
    print(match.groupdict())
```

## Security: Preventing ReDoS (Regular Expression Denial of Service)

ReDoS occurs when a regular expression contains nested quantifiers that cause **catastrophic backtracking** on mismatched strings. An attacker can exploit this to freeze CPU execution.

### 1. Avoid Nested Quantifiers
* **Vulnerable Pattern**: `(a+)+` or `(a|a+)+`
  If matched against a string like `aaaaaaaaaaaaaaaaaaaaaaaaab` (containing many 'a's but ending with 'b'), the regex engine tries every combination of groups, leading to exponential execution time.
* **Safe Alternative**: Simplify the pattern to avoid overlapping repetition. Use `a+` instead.

### 2. Guard Against User-Supplied Regex
If users can supply their own regular expressions, do not compile them directly with `re`. Use external libraries like `google-re2` (which uses a linear-time regex engine) or implement a timeout monitor.

```python
# Example of catastrophic backtracking in Python's standard 're':
import re
import time

unsafe_regex = re.compile(r"(a+)+$")

start = time.time()
# Mismatch at the end on a long string
unsafe_regex.search("a" * 25 + "!")
print(f"Elapsed time: {time.time() - start:.4f} seconds")  # Can take seconds/minutes to fail
```
