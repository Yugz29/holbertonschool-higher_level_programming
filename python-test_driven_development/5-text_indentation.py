#!/usr/bin/python3
"""
This module defines a function that prints a text with 2 new lines
after each occurrence of '.', '?', or ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ?, :

    Args:
        text (str): The text to print

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    segment = ""
    for char in text:
        segment += char
        if char in ".?:":
            print(segment.strip(), end="")
            print()
            print()
            segment = ""
    if segment:
        print(segment.strip(), end="")
