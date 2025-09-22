#!/usr/bin/python3
"""
Module 4-inherits_from

This module defines a function that checks if an object
is an instance of a subclass (directly or indirectly)
of a specified class, but not an exact instance of that class.
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherits
    (directly or indirectly) from a_class, but not if it is
    exactly an instance of a_class.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
              False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
