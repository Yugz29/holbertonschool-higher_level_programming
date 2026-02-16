# Python More Data Structures

## Overview

This directory contains exercises focused on **advanced Python data structures** from the Holberton School Higher Level Programming track.

The exercises cover dictionaries, sets, matrices, and various operations on these data structures, helping to build deeper understanding and manipulation skills.

---

## Learning Focus

This module demonstrates how to:

* Manipulate lists, sets, and dictionaries
* Perform union, intersection, and difference operations
* Access, update, and delete dictionary keys and values
* Sort dictionary keys and iterate in order
* Apply transformations on dictionaries and lists
* Work with matrices and multi-dimensional data

---

## Files and Tasks

| File                           | Purpose                                                 |
| ------------------------------ | ------------------------------------------------------- |
| `0-square_matrix_simple.py`    | Create and manipulate simple square matrices            |
| `1-search_replace.py`          | Search and replace elements in a list or matrix         |
| `2-uniq_add.py`                | Add unique integers from a list using sets              |
| `3-common_elements.py`         | Return common elements between two lists                |
| `4-only_diff_elements.py`      | Return elements only in one list (symmetric difference) |
| `5-number_keys.py`             | Count the number of keys in a dictionary                |
| `6-print_sorted_dictionary.py` | Print dictionary keys and values in sorted order        |
| `7-update_dictionary.py`       | Add or replace key/value pairs in a dictionary          |
| `8-simple_delete.py`           | Delete keys from a dictionary safely                    |
| `9-multiply_by_2.py`           | Multiply dictionary values by 2, return new dictionary  |
| `10-best_score.py`             | Determine the key with the best score in a dictionary   |
| `11-multiply_list_map.py`      | Multiply all elements in a list using `map()`           |
| `12-roman_to_int.py`           | Convert Roman numerals to integers                      |

---

## Example Snippet

Example of finding common elements between two lists:

```python
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))
print(common)  # Outputs: [3, 4]
```

This demonstrates using set intersection to find common elements.

---

## Skills Demonstrated

* Manipulating Python lists, dictionaries, and sets
* Performing set operations: union, intersection, difference
* Updating, deleting, and iterating dictionaries
* Working with matrices and multi-dimensional lists
* Applying Pythonic best practices for data manipulation

---

## Why This Matters

Mastering advanced data structures in Python is important because:

* Dictionaries and sets are key for efficient data storage and lookup
* Matrix manipulation is essential for mathematical and algorithmic applications
* These skills are foundational for algorithms, data analysis, and real-world programming
