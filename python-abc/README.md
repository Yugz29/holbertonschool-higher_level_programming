# Python ABC Exercises

## Overview

This directory contains exercises focused on **Python object-oriented programming (OOP)** and **abstract base classes (ABC)** from the Holberton School Higher Level Programming track.

The exercises aim to teach key OOP concepts such as inheritance, polymorphism, and duck typing using Python. Students practice designing classes, implementing methods, and understanding relationships between objects.

---

## Learning Focus

This module demonstrates:

* Creating classes and defining methods
* Using inheritance to extend classes
* Implementing polymorphism and duck typing
* Working with abstract base classes (ABCs)
* Handling exceptions and iterators
* Combining OOP principles with Pythonic design patterns

---

## Files and Tasks

| File                         | Purpose                                                                 |
| ---------------------------- | ----------------------------------------------------------------------- |
| `task_00_abc.py`             | Define base classes and inheritance (Animal, Dog, Cat)                  |
| `task_01_duck_typing.py`     | Demonstrate duck typing in Python                                       |
| `task_02_verboselist.py`     | Implement a list class that logs actions or returns values              |
| `task_03_countediterator.py` | Create an iterator with counting functionality and exception handling   |
| `task_04_flyingfish.py`      | Implement multi-level inheritance (Fish, Bird, FlyingFish)              |
| `task_05_dragon.py`          | Extend inheritance and implement additional behavior for a Dragon class |
| `README.md`                  | Overview of the Python ABC exercises                                    |

> Each file contains comments explaining the purpose and expected behavior.

---

## Example Snippet

Example of a simple class with inheritance:

```python
class Animal:
    def speak(self):
        print("Some generic sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

my_dog = Dog()
my_dog.speak()  # Outputs: Woof!
```

This snippet demonstrates inheritance and method overriding.

---

## Skills Demonstrated

* Understanding and implementing OOP concepts in Python
* Using inheritance and polymorphism effectively
* Applying abstract base classes to enforce structure
* Implementing duck typing and iterators
* Handling exceptions in a Pythonic way

---

## Why This Matters

Mastering OOP and ABCs in Python is important because:

* It lays the foundation for scalable and maintainable code
* Enables building complex systems with clear class hierarchies
* Provides understanding of polymorphism and dynamic behavior
* Prepares for advanced Python programming and real-world application development
