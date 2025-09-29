#!/usr/bin/python3
"""This module provides a function to add text to the end of a file"""


def append_write(filename="", text=""):
    """
    Adds text to the end of a file and returns the number of
    characters written.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
