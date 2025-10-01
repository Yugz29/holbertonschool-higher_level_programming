#!/usr/bin/python3
"""
This module provides a function to load a Python object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Load an object from a JSON file.

    Returns:
        The Python object deserialized from the JSON file.
    """
    with open(filename, "r") as f:
        obj = json.load(f)
        return obj
