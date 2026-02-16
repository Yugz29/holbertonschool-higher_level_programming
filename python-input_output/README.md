# Python Input/Output

## Overview

This directory contains exercises focused on **file input/output and JSON handling in Python** from the Holberton School Higher Level Programming track.

The exercises teach how to read and write files, serialize and deserialize JSON, and manipulate objects for storage and retrieval.

---

## Learning Focus

This module demonstrates:

* Reading from and writing to text files
* Appending to files safely
* Using Python's `with open()` context manager
* Converting objects to JSON strings and saving to files
* Loading JSON strings from files and converting to Python objects
* Working with custom classes and serializing their attributes
* Implementing Pascal's triangle generation

---

## Files and Tasks

| File                           | Purpose                                                      |
| ------------------------------ | ------------------------------------------------------------ |
| `0-read_file.py`               | Read and print the contents of a file                        |
| `1-write_file.py`              | Write text to a file                                         |
| `2-append_write.py`            | Append text to an existing file                              |
| `3-to_json_string.py`          | Convert Python objects to JSON string                        |
| `4-from_json_string.py`        | Convert JSON string back to Python objects                   |
| `5-save_to_json_file.py`       | Save Python objects to a JSON file                           |
| `6-load_from_json_file.py`     | Load Python objects from a JSON file                         |
| `7-add_item.py`                | Add items to a list stored in JSON file                      |
| `8-class_to_json.py`           | Convert class instance attributes to dictionary/JSON         |
| `8-my_class.py`                | Example of class conversion to dictionary                    |
| `8-my_class_2.py`              | Another class serialization example                          |
| `9-student.py`                 | Define a Student class                                       |
| `10-student.py`                | Implement methods for Student class                          |
| `11-student.py`                | Reload Student instance from JSON file                       |
| `12-pascal_triangle.py`        | Generate Pascal's triangle up to a given number of rows      |
| `README.md`                    | Overview of input/output exercises                           |
| Misc files (`*.txt`, `*.json`) | Example files used for reading, writing, and JSON operations |

---

## Example Snippet

Example of reading a file and printing its contents:

```python
with open("my_first_file.txt", "r") as f:
    contents = f.read()
    print(contents)
```

Example of saving an object to JSON:

```python
import json

my_dict = {"name": "Alice", "age": 25}
with open("my_dict.json", "w") as f:
    json.dump(my_dict, f)
```

---

## Skills Demonstrated

* Reading, writing, and appending files in Python
* JSON serialization and deserialization
* Using Python's context managers for safe file handling
* Working with custom class objects and saving/loading them
* Implementing algorithmic functions like Pascal's triangle

---

## Why This Matters

Mastering file input/output and JSON handling is important because:

* Files are the main way programs store persistent data
* JSON is a universal format for data exchange
* Proper file handling ensures data integrity and program stability
* These skills are essential for real-world Python applications, APIs, and data processing
