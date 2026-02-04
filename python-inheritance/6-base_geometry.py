#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class with area method"""
    def area(self):
        """Raises an exception for unimplemented area method"""
        raise Exception("area() is not implemented")
    pass
