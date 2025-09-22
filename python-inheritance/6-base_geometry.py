#!/usr/bin/python3
"""
Module base_geometry

This module defines an empty BaseGeometry class.
It can be used as a base class for future geometric shapes.
"""


class BaseGeometry:
    """
    Base class for geometry-related classes.

    Contains a placeholder method 'area' that should be
    overridden by subclasses.
    """

    def area(self):
        """
        Placeholder method for calculating the area of a shape.

        Raises:
            Exception: Always raises an Exception because the method
                       is not implemented in the base class.
        """
        raise Exception("area() is not implemented")
