# Python Everything is Object

## Overview

This directory contains exercises from the Holberton School Higher Level Programming track exploring the concept that **everything in Python is an object**.

The exercises mainly consist of answering conceptual questions and implementing small Python scripts that demonstrate object behavior, type checking, and Python's class model.

---

## Learning Focus

This module demonstrates:

* Understanding that all data types in Python are objects
* Examining object types and identities
* Using `type()` and `id()` functions
* Copying and manipulating objects
* Understanding object references and mutability
* Applying Pythonic thinking to object behavior

---

## Files and Tasks

| File                              | Purpose                                                                   |
| --------------------------------- | ------------------------------------------------------------------------- |
| `0-answer.txt` to `28-answer.txt` | Answers to theory questions about Python objects and types                |
| `19-copy_list.py`                 | Function to copy a list, demonstrating object references and independence |

> Each answer file contains the response to a specific question, explaining Python's object model.

---

## Example Snippet

Example of checking object type and identity:

```python
my_list = [1, 2, 3]
print(type(my_list))  # <class 'list'>
print(id(my_list))    # Unique identifier for the object
```

This demonstrates that lists are objects with unique identities in memory.

---

## Skills Demonstrated

* Understanding Python's object-oriented model
* Working with data types and their identities
* Copying objects and understanding references
* Differentiating mutable and immutable objects
* Reading and writing concise explanations of object behavior

---

## Why This Matters

Mastering the concept that everything is an object in Python is critical because:

* It forms the foundation for Python's OOP features
* It improves understanding of variable assignment and memory handling
* It helps prevent common pitfalls with mutable vs immutable objects
* It prepares for advanced topics like custom classes, inheritance, and object manipulation
