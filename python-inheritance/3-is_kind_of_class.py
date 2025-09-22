#!/usr/bin/python3
"""
Module 3-is_kind_of_class

This module defines a function that checks if an object
is an instance of a specified class or any of its subclasses.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of the specified class
    or a subclass thereof, otherwise returns False.
    """

    return isinstance(obj, a_class)
