#!/usr/bin/python3
"""
Module that defines a Student class for representing student information.
"""


class Student:
    """
    Class Student that defines a student with first name, last name, and age.
    Provides a method to retrieve a dictionary representation of the instance.
    """
    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary containing the specified attributes,
            or all attributes if attrs is None.
        """
        if attrs is None:
            return self.__dict__
        filtered = {}
        for attribut in attrs:
            if hasattr(self, attribut):
                filtered[attribut] = getattr(self, attribut)
            return filtered
