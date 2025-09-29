#!/usr/bin/python3
"""
This module provides a function to convert a Python object into a
JSON string representation
"""
import json


def to_json_string(my_obj):
    """
    Convert a Python object to a JSON string

    Returns:
        str: The JSON string representation of the object
    """
    json_str = json.dumps(my_obj)
    return json_str
