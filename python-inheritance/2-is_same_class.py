#!/usr/bin/python3
"""Define a class Rectangle"""


def is_same_class(obj, a_class):
    """
    Return True if the object is exactly an instance of the specified class
        obj: The object to check
        a_class: The class to match the type of obj to
    """
    return type(obj) is a_class
