#!/usr/bin/python3
"""Task 0: Abstract Base Class (ABC)"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals"""

    @abstractmethod
    def sound(self):
        """Return the sound by the animal"""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal"""
    def sound(self):
        """Return the sound of a dog"""
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal"""
    def sound(self):
        """Return the sound of a cat"""
        return "Meow"
