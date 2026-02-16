# Python Import Modules

## Overview

This directory contains exercises focused on **Python modules and importing** from the Holberton School Higher Level Programming track.

The exercises aim to teach how to organize code in modules, import functions and variables, and create reusable and modular Python programs.

---

## Learning Focus

This module demonstrates:

* Creating Python modules with functions and variables
* Importing specific functions or variables from modules
* Using `from module import ...` and `import module` syntax
* Writing scripts that utilize imported code
* Understanding Python's module search path
* Using modules to organize calculations, additions, and utilities

---

## Files and Tasks

| File                    | Purpose                                                  |
| ----------------------- | -------------------------------------------------------- |
| `0-add.py`              | Simple addition function to be imported                  |
| `1-calculation.py`      | Module performing basic calculations                     |
| `2-args.py`             | Handling command-line arguments in scripts using imports |
| `3-infinite_add.py`     | Adding multiple numbers from command-line arguments      |
| `4-hidden_discovery.py` | Discover hidden variables and functions in modules       |
| `5-variable_load.py`    | Import and print variables from another module           |
| `add_0.py`              | Demonstrate module usage and printing results            |
| `calculator_1.py`       | Calculator module with renamed functions for import      |
| `variable_load_5.py`    | Advanced variable import and usage example               |
| `README.md`             | Overview of module import exercises                      |

---

## Example Snippet

Example of importing a function from another module:

```python
# in add.py

def add(a, b):
    return a + b

# in main.py
from add import add

result = add(5, 3)
print(result)  # Outputs: 8
```

This demonstrates defining a function in a module and importing it into another script.

---

## Skills Demonstrated

* Writing modular Python code using modules and imports
* Organizing reusable functions and variables
* Understanding module search paths and imports
* Using command-line arguments with imported code
* Applying Pythonic best practices for code reuse

---

## Why This Matters

Mastering Python modules and imports is important because:

* It allows for clean, organized, and maintainable code
* It promotes code reuse across multiple scripts and projects
* It forms the basis for Python packages and libraries
* It is essential for building scalable and professional Python applications
