# Python Exceptions

## Overview

This directory contains exercises focused on **exception handling in Python** from the Holberton School Higher Level Programming track.

The exercises aim to teach how to write safe code using `try`, `except`, `finally` blocks, raise exceptions, and handle errors gracefully while maintaining program stability.

---

## Learning Focus

This module demonstrates:

* Using `try` and `except` to catch and handle exceptions
* Using `finally` blocks to ensure cleanup actions
* Raising exceptions intentionally with `raise`
* Handling multiple types of exceptions
* Performing safe operations on lists, integers, and divisions
* Writing robust code that handles unexpected inputs

---

## Files and Tasks

| File                            | Purpose                                                      |
| ------------------------------- | ------------------------------------------------------------ |
| `0-safe_print_list.py`          | Print all elements of a list safely with exception handling  |
| `1-safe_print_integer.py`       | Print an integer safely, handling type errors                |
| `2-safe_print_list_integers.py` | Print a list of integers safely, ignoring invalid elements   |
| `3-safe_print_division.py`      | Divide two numbers safely, handling division errors          |
| `4-list_division.py`            | Divide elements of two lists safely, handling all exceptions |
| `5-raise_exception.py`          | Demonstrate raising a generic exception                      |
| `6-raise_exception_msg.py`      | Demonstrate raising an exception with a custom message       |

---

## Example Snippet

Example of safe division with exception handling:

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None

print(safe_divide(10, 2))  # Outputs: 5.0
print(safe_divide(10, 0))  # Outputs: Cannot divide by zero
```

This snippet demonstrates catching a specific exception to prevent program crash.

---

## Skills Demonstrated

* Writing Python code that handles runtime errors gracefully
* Using `try`, `except`, `finally` effectively
* Raising exceptions intentionally to enforce constraints
* Ensuring program stability and safe data operations
* Understanding exception hierarchy and best practices in Python

---

## Why This Matters

Mastering exception handling is important because:

* It prevents crashes and ensures programs behave predictably
* It allows writing robust, maintainable code
* It improves debugging and error reporting
* It is essential for real-world applications that handle unpredictable inputs
