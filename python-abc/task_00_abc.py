#!/usr/bin/python3
"""
Example of ABC with Animal, Dog, and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    ABC representing an Animal
    """

    @abstractmethod
    def sound(self):
        """
        Define the sound for an Animal
        """
        pass

class Dog(Animal):
    """
    Dog class inherting from Animal
    """

    def sound(self):
        """
        Return the sound of a Dog
        """
        return "Bark"
    
class Cat(Animal):
    """
    Cat class inherting from Animal
    """

    def sound(self):
        """
        Return the sound of a Cat
        """
        return "Meow"
