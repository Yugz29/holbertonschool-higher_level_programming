#!/usr/bin/python3
"""
Module that defines a Student class for representing student information.
"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns the dictionary representation of the Student instance.
        """
        return self.__dict__
