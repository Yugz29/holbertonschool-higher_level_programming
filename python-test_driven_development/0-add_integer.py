#!/usr/bin/python3
"""
This module defines the function add_integer.
It adds two integers, casting floats if necessary.
It raises a TypeError if inputs are not integers or floats.
"""


def add_integer(a, b=98):
    """
    Returns the sum of a and b as integers.
    Floats are casted to integers before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    try:
        a_int = int(a)
        b_int = int(b)
    except (OverflowError, ValueError):
        raise TypeError("a must be an integer"
                        if isinstance(a, float) else "b must be an integer")
    return a_int + b_int
