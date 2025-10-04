#!/usr/bin/env python3
"""
Module providing a CustomObject class with methods to
serialize and deserialize instances using pickle.
"""
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """Initialize a new CustomObject instance.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Indicates if the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the attributes of the object in a formatted manner."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current object and save it to a file.

        Returns:
            None if an exception, otherwise the object is saved successfully.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return a CustomObject instance from a file.

        Returns:
            CustomObject instance if successful, None if an exception occurs.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj
        except Exception:
            return None
