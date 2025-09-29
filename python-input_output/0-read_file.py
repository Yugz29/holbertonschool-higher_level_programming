#!/usr/bin/python3
"""Module for reading and displaying the contents of a text file"""


def read_file(filename=""):
    """Reads a text file and displays its contents on standard output

    Returns:
        This function does not return anything, it only displays the content.
    """
    with open(filename, "r", encoding="utf-8") as f:
        contenu = f.read()
        print(contenu, end="")
