#!/usr/bin/python3
"""
Module lookup

This module provides a helper function to list all
attributes and methods available for a given object
using Python's built-in dir() function.
"""


def lookup(obj):
    """
    Prints all attributes and methods available for an object.

    Returns:
        None: The function only prints the result of dir(obj).
    """
    print(dir(obj))
