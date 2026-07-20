---
title: Testing
tags: [testing, unittest, pytest, doctest, tdd, mocking]
status: complete
source: Official Python docs, unittest module
last_updated: 2026-07-20
---

# Testing

Testing validates code correctness, prevents regressions, and helps document usage. Python offers robust built-in modules for testing alongside highly popular third-party alternatives.

## The `unittest` Module

Python's built-in unit testing framework requires test cases to inherit from `unittest.TestCase`.

```python
import unittest

# Code to be tested
def add_positive_numbers(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive numbers")
    return a + b

# Test Case class
class TestMathOperations(unittest.TestCase):
    def setUp(self):
        # Runs BEFORE every test method; perfect for setup/fixture creation
        self.valid_a = 5
        self.valid_b = 10

    def tearDown(self):
        # Runs AFTER every test method; perfect for cleanup
        pass

    def test_addition_success(self):
        result = add_positive_numbers(self.valid_a, self.valid_b)
        self.assertEqual(result, 15)

    def test_addition_raises_value_error(self):
        # Assert that a specific exception is raised
        with self.assertRaises(ValueError):
            add_positive_numbers(-1, 5)

if __name__ == "__main__":
    unittest.main()
```

## The `doctest` Module

The `doctest` module searches for pieces of text that look like interactive Python sessions inside docstrings, executing them to verify they work exactly as shown.

```python
def multiply(a, b):
    """
    Multiplies two numbers and returns the result.

    >>> multiply(2, 3)
    6
    >>> multiply(-1, 5)
    -5
    """
    return a * b

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

## Testing Best Practices and Security

### 1. Test Isolation and Mocking
Tests should run in complete isolation from the external network, filesystem, or database to ensure speed, determinism, and safety. Use `unittest.mock` to simulate external services.
```python
from unittest.mock import patch
import unittest

def fetch_api_status():
    # Imagine this performs a real HTTP request
    import urllib.request
    with urllib.request.urlopen("https://api.example.com/status") as response:
        return response.read().decode('utf-8')

class TestExternalService(unittest.TestCase):
    @patch('urllib.request.urlopen')
    def test_fetch_status_mocked(self, mock_urlopen):
        # Set up mock response
        mock_response = mock_urlopen.return_value.__enter__.return_value
        mock_response.read.return_value = b"OK"
        
        self.assertEqual(fetch_api_status(), "OK")
```

### 2. Avoid Executing Unsanitized Test Code
Do not use `eval()` or dynamically load arbitrary modules when scaffolding test files, especially when running automated CI/CD pipelines as non-privileged users.

## External Libraries and Methodologies

- **Pytest**: A popular PyPI framework with simple syntax (no classes required, uses plain `assert` statements) and advanced fixture capabilities.
- **TDD (Test-Driven Development)**: A design methodology where you write the test *before* implementing the feature code (Red-Green-Refactor loop).
