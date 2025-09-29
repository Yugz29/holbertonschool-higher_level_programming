#!/usr/bin/python3
"""This module provides a function for writing text to a file.
"""


def write_file(filename="", text=""):
    """Writes text to a file and returns the number of characters written.

    Returns:
    int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
