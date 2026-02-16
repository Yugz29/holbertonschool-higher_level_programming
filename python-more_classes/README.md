# Python More Classes

## Overview

This directory contains exercises focused on **advanced Python class features** from the Holberton School Higher Level Programming track.

The exercises cover object attributes, methods, special methods, class attributes, class methods, and comparisons. The goal is to deepen understanding of Python classes and object-oriented programming.

---

## Learning Focus

This module demonstrates:

* Defining classes with instance and class attributes
* Implementing special methods (`__str__`, `__repr__`, `__del__`)
* Calculating area and perimeter for geometric shapes
* Keeping track of the number of instances of a class
* Comparing objects using class methods
* Applying Pythonic OOP best practices

---

## Files and Tasks

| File             | Purpose                                                    |
| ---------------- | ---------------------------------------------------------- |
| `0-rectangle.py` | Basic rectangle class definition                           |
| `1-rectangle.py` | Add `area` and `perimeter` methods                         |
| `2-rectangle.py` | Enhanced area and perimeter calculation                    |
| `3-rectangle.py` | Implement `__str__` for string representation              |
| `4-rectangle.py` | Implement `__repr__` for unambiguous object representation |
| `5-rectangle.py` | Implement `__del__` to handle object deletion              |
| `6-rectangle.py` | Add class attribute to track number of instances           |
| `7-rectangle.py` | Code style fixes and improvements                          |
| `8-rectangle.py` | Add `bigger_or_equal` method to compare rectangles         |
| `9-rectangle.py` | Add class method and other enhancements                    |

---

## Example Snippet

Example of a class with area calculation and string representation:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

rect = Rectangle(4, 5)
print(rect)        # Outputs: Rectangle(width=4, height=5)
print(rect.area()) # Outputs: 20
```

---


## Skills Demonstrated

* Defining Python classes with instance and class attributes
* Implementing special methods for string representation and deletion
* Creating reusable methods for calculations (area, perimeter)
* Tracking class instances
* Comparing objects using class methods
* Writing clean, maintainable, Pythonic class code

---

## Why This Matters

Mastering advanced Python class features is important because:

* It enables building robust, reusable, and maintainable objects
* Special methods improve readability and usability of objects
* Class attributes and methods allow flexible design patterns
* These skills are foundational for object-oriented design and real-world Python applications
