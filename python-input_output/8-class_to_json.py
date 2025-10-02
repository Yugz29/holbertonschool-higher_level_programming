#!/usr/bin/python3
"""Module for converting a class object to a dictionary representation."""


def class_to_json(obj):
    """Return the dictionary representation of a class instance.

    Returns:
        dict: The dictionary representation of the instance attributes.
    """
    return obj.__dict__
