# Python Serialization

## Overview

This directory contains exercises focused on **serialization in Python** from the Holberton School Higher Level Programming track.

The exercises teach how to convert Python objects to a format that can be stored or transmitted, and how to reconstruct them, using formats such as JSON, Pickle, CSV, and XML.

---

## Learning Focus

This module demonstrates:

* Converting Python objects to JSON and back
* Using the `pickle` module to serialize and deserialize Python objects
* Converting CSV data to JSON format
* Serializing and deserializing data in XML format
* Understanding the differences and use cases of each serialization method
* Preserving object state across sessions or for data transmission

---

## Files and Tasks

| File                             | Purpose                                             |
| -------------------------------- | --------------------------------------------------- |
| `task_00_basic_serialization.py` | Serialize and deserialize Python objects using JSON |
| `task_01_pickle.py`              | Serialize a custom class object using `pickle`      |
| `task_02_csv.py`                 | Convert CSV files to JSON format                    |
| `task_03_xml.py`                 | Serialize and deserialize objects in XML format     |

---

## Example Snippet

Example of JSON serialization:

```python
import json

my_data = {'name': 'Alice', 'age': 25}
serialized = json.dumps(my_data)  # Serialize to JSON string
print(serialized)

deserialized = json.loads(serialized)  # Deserialize back to Python object
print(deserialized)
```

Example of Pickle serialization:

```python
import pickle

class CustomObject:
    def __init__(self, value):
        self.value = value

obj = CustomObject(42)
serialized_obj = pickle.dumps(obj)  # Serialize object
restored_obj = pickle.loads(serialized_obj)  # Deserialize object
print(restored_obj.value)  # Outputs: 42
```

---

## Skills Demonstrated

* Serializing and deserializing Python objects using JSON and Pickle
* Converting between CSV and JSON data
* Working with XML for data serialization
* Preserving object state for storage or transmission
* Understanding best practices and limitations of each serialization format

---

## Why This Matters

Mastering serialization in Python is important because:

* It allows persistent storage of object state
* Enables data exchange between systems and languages
* Essential for saving program state, caching, and API data handling
* Forms the foundation for advanced topics like data pipelines and distributed applications
