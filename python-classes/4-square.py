#!/usr/bin/python3

"""A module that defines a Square class."""


class Square:
    """A class that defines a square by its size."""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square"""
        return self.__size * self.__size