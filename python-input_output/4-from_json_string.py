#!/usr/bin/python3
"""
This module provides a function to convert a JSON string into
its corresponding Python object using the built-in `json` library
"""
import json


def from_json_string(my_str):
    """
    Convert a JSON-formatted string into a corresponding Python object

    Returns:
        object: The Python object represented by the JSON string
    """
    obj = json.loads(my_str)
    return obj
