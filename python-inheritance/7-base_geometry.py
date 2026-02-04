#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class with area method"""
    def __init__(self):
        pass

    def area(self):
        """Raises an exception for unimplemented area method"""
        raise Exception("area() is not implemented")

    """Validates that value is a positive integer"""
    def integer_validator(self, name, value):
        """Validates that value is a positive integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
