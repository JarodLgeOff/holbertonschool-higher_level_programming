#!/usr/bin/python3
"""
Adds two integers or floats and returns an integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.
    Args:
        a (int or float): first number.
        b (int or float): second number.
    Returns:
        int: the addition of a and b.
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
