#!/usr/bin/python3
"""Module defining a Square class that inherits from Rectangle"""
Reactangle = __import__('9-rectangle').Rectangle


class Square(Reactangle):
    """Class representing a square, inheriting from BaseGeometry"""

    def __init__(self, size):
        """Initialize a square with validated size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size

