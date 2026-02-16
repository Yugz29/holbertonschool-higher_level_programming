# Python Data Structures Exercises

## Overview

This directory contains exercises focused on **Python data structures** from the Holberton School Higher Level Programming track.

The exercises cover lists, tuples, matrices, and operations on these data structures. The goal is to teach manipulation, indexing, iteration, and applying Pythonic practices to handle data efficiently.

---

## Learning Focus

This module demonstrates how to:

* Access elements in lists and tuples
* Modify, add, and delete elements in lists
* Use loops and conditions with data structures
* Create and manipulate matrices
* Work with multiple return values
* Apply defensive programming techniques for edge cases

---

## Files and Tasks

| File                               | Purpose                                                       |
| ---------------------------------- | ------------------------------------------------------------- |
| `0-print_list_integer.py`          | Print all integers in a list                                  |
| `1-element_at.py`                  | Return an element at a given index with validation            |
| `2-replace_in_list.py`             | Replace an element at a specific index                        |
| `3-print_reversed_list_integer.py` | Print a list in reverse order                                 |
| `4-new_in_list.py`                 | Return a new list with replaced values                        |
| `5-no_c.py`                        | Remove all occurrences of 'c' from a list of characters       |
| `6-print_matrix_integer.py`        | Print a matrix of integers row by row                         |
| `7-add_tuple.py`                   | Add two tuples element-wise                                   |
| `8-multiple_returns.py`            | Return multiple values from a list (length and first element) |
| `9-max_integer.py`                 | Find and return the maximum integer in a list                 |
| `10-divisible_by_2.py`             | Return elements divisible by 2 from a list                    |
| `11-delete_at.py`                  | Delete an element at a specific index                         |
| `12-switch.py`                     | Swap two elements in a list                                   |

---

## Example Snippet

Example of accessing and printing a list element:

```python
my_list = [1, 2, 3, 4]
index = 2
if 0 <= index < len(my_list):
    print(my_list[index])  # Outputs: 3
```

This demonstrates safe indexing with validation.

---

## Skills Demonstrated

* Manipulating lists, tuples, and matrices
* Indexing, slicing, and element replacement
* Iterating with loops and conditions
* Returning multiple values from functions
* Writing defensive and Pythonic code

---

## Why This Matters

Mastering Python data structures is essential because:

* Lists and tuples are fundamental for data storage and manipulation
* They form the basis for algorithms and more complex data structures
* Efficient manipulation improves program performance
* Provides a foundation for advanced Python programming and real-world applications
