#!/usr/bin/python3
"""
Module square
Defines an empty class Square.
"""


class Square:
    """Represents an empty Square class.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, valeur):
        if type(valeur) is not int:
            raise TypeError("size must be an integer")
        if valeur < 0:
            raise ValueError("size must be >= 0")
        self.__size = valeur

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, valeur):
        if (
            not isinstance(valeur, tuple)
            or len(valeur) != 2
            or not all(isinstance(i, int) for i in valeur)
            or not all(i >= 0 for i in valeur)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = valeur

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__position[1]):
            print("")
            return
        for _ in range(self.__size):
            print("" * self.__position[0] + "#" * self.__size)
