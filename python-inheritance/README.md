# Python Inheritance Exercises

## Overview

This directory contains exercises focused on **inheritance in Python** from the Holberton School Higher Level Programming track.

The exercises teach how to create classes that inherit attributes and methods from other classes, override behavior, and implement polymorphism.

---

## Learning Focus

This module demonstrates:

* Defining base classes and derived classes
* Using `isinstance()` and `type()` to check class types
* Overriding methods in derived classes
* Applying exception handling in class methods
* Implementing simple geometric classes (`BaseGeometry`, `Rectangle`, `Square`)
* Working with Python’s object-oriented principles in practice

---

## Files and Tasks

| File                    | Purpose                                                                       |
| ----------------------- | ----------------------------------------------------------------------------- |
| `0-lookup.py`           | List available attributes and methods of an object                            |
| `1-my_list.py`          | Extend list with custom behavior and printing sorted list                     |
| `2-is_same_class.py`    | Check if an object is exactly an instance of a given class                    |
| `3-is_kind_of_class.py` | Check if an object is an instance or subclass of a class using `isinstance()` |
| `4-inherits_from.py`    | Check if a class inherits from another using `type()` and `isinstance()`      |
| `5-base_geometry.py`    | Define a base geometry class                                                  |
| `6-base_geometry.py`    | Raise exceptions for unimplemented methods in base class                      |
| `7-base_geometry.py`    | Add type validation methods                                                   |
| `8-rectangle.py`        | Implement a Rectangle class inheriting from BaseGeometry                      |
| `9-rectangle.py`        | Code style fixes and improvements                                             |
| `10-square.py`          | Implement a Square class inheriting from Rectangle                            |
| `11-square.py`          | Add method to return area of Square                                           |

---

## Example Snippet

Example of inheritance in Python:

```python
class Base:
    def greet(self):
        print("Hello from Base")

class Derived(Base):
    def greet(self):
        print("Hello from Derived")

obj = Derived()
obj.greet()  # Outputs: Hello from Derived
```

This demonstrates overriding a method in a derived class.

---

## Skills Demonstrated

* Implementing class inheritance in Python
* Overriding methods and extending behavior
* Checking class types and instances
* Handling unimplemented methods with exceptions
* Designing simple object-oriented class hierarchies

---

## Why This Matters

Mastering inheritance in Python is important because:

* It allows code reuse and modularity
* It forms the foundation for object-oriented programming
* It enables polymorphism and flexible design
* It is essential for building complex and maintainable Python applications
