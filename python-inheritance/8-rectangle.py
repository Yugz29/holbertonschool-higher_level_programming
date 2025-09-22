#!/usr/bin/python3
"""
Module 8-rectangle

Defines the Rectangle class that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle shape.

    Inherits from BaseGeometry. Width and height must be
    positive integers validated using integer_validator.
    """

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.

        Raises:
            TypeError: If width or height are not integers
            ValueError: If width or height <= 0
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
