# Python Test-Driven Development

## Overview

This directory contains exercises focused on **test-driven development (TDD) in Python** from the Holberton School Higher Level Programming track.

The exercises emphasize writing Python functions and modules alongside tests to ensure correctness, robustness, and adherence to specifications.

---

## Learning Focus

This module demonstrates:

* Writing Python functions following TDD principles
* Using `doctest` and other testing methods
* Validating input types and values
* Handling edge cases and exceptions
* Writing clean, maintainable, and testable code
* Ensuring functions produce expected results through automated tests

---

## Files and Tasks

| File                    | Purpose                                                      |
| ----------------------- | ------------------------------------------------------------ |
| `0-add_integer.py`      | Add two integers with type checking                          |
| `2-matrix_divided.py`   | Divide all elements of a matrix with validation              |
| `3-say_my_name.py`      | Print formatted name with validation                         |
| `4-print_square.py`     | Print a square of a given size using `#`                     |
| `5-text_indentation.py` | Print text with proper indentation after `.`, `?`, `!`       |
| `6-max_integer.py`      | Return the maximum integer in a list                         |
| `tests/`                | Folder containing `doctest` and unit tests for each function |

---

## Example Snippet

Example of a function with a `doctest`:

```python
def add_integer(a, b=98):
    """
    Adds two integers.

    >>> add_integer(1, 2)
    3
    >>> add_integer(10)
    108
    >>> add_integer(1.5, 2.5)
    3
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

---

## Skills Demonstrated

* Test-driven development in Python
* Writing and validating functions with doctests
* Handling invalid inputs and edge cases
* Ensuring correctness through automated testing
* Writing clean, maintainable, and testable Python code

---

## Why This Matters

Mastering TDD in Python is important because:

* It ensures your code is correct and robust from the start
* Reduces bugs and regressions in larger projects
* Encourages writing modular and maintainable code
* Provides confidence in refactoring and extending codebases
* Is a foundational practice for professional software development
