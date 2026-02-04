#!/usr/bin/python3
"""Define a class Rectangle"""


def inherits_from(obj, a_class):
    """Function that checks if an object is an instance of a class that
    inherited (directly or indirectly) from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to be checked against.
    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class; otherwise
        False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
