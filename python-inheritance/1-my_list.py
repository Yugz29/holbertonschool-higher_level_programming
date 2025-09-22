#!/usr/bin/python3
"""
Module my_list

This module defines the MyList class, which extends
the built-in Python list with an extra method.
"""


class MyList(list):
    """
    MyList class that inherits from the built-in list.
    Adds a method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending sorted order.

        sorted() creates and returns a new sorted list.
        """
        print(sorted(self))
