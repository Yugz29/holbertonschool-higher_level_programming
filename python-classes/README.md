# Python Classes Exercises

## Overview

This directory contains exercises focused on **Python classes** from the Holberton School Higher Level Programming track.

The exercises aim to teach how to define classes, create attributes, implement methods, and use object-oriented principles in Python. The focus is on building reusable, modular, and maintainable code using classes.

---

## Learning Focus

This module demonstrates:

* Defining Python classes with attributes and methods
* Using constructors (`__init__`) to initialize objects
* Implementing getters and setters
* Raising and handling exceptions for invalid input
* Creating custom methods for behavior (e.g., `my_print`)
* Applying OOP principles in a Pythonic way

---

## Files and Tasks

| File          | Purpose                                                           |
| ------------- | ----------------------------------------------------------------- |
| `0-square.py` | Basic class definition for a square                               |
| `1-square.py` | Adding attributes for size and position                           |
| `2-square.py` | Implementing validation and raising errors for invalid attributes |
| `3-square.py` | Code style fixes and improvements                                 |
| `4-square.py` | Adding getter and setter methods for attributes                   |
| `5-square.py` | Implementing a method to print the square (`my_print`)            |
| `6-square.py` | Removed (no longer used)                                          |

---

## Example Snippet

Example of a simple class with attribute and method:

```python
class Square:
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.size ** 2

my_square = Square(4)
print(my_square.area())  # Outputs: 16
```

This snippet demonstrates defining a class, initializing an attribute, and creating a method.

---

## Skills Demonstrated

* Defining and instantiating Python classes
* Using attributes and methods effectively
* Validating input and raising exceptions
* Creating modular, reusable code with OOP
* Applying Pythonic best practices for classes

---

## Why This Matters

Mastering Python classes is important because:

* Classes enable structured and maintainable code
* They form the foundation for object-oriented programming
* They prepare you for building complex systems and applications
* They provide a solid base for learning inheritance, polymorphism, and advanced OOP concepts
