#!/usr/bin/env python3
"""
Duck Typing Exercise with Abstract Base Classes
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    ABC for Shapes
    """
    @abstractmethod
    def area(self):
        """
        Calculates and returns the area of the shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculates and returns the perimeter of the shape
        """
        pass


class Circle(Shape):
    """
    Implementation of shape for Circle
    """
    def __init__(self, radius):
        """
        Initialize a Circle with a radius
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of Circle
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculates the perimeter of Circle
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Implementation of shape for Rectangle
    """
    def __init__(self, width, height):
        """
        Initialize a Rectangle with width and height
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates the area of Rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of Rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of all shapes
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
