#!/bin/usr/python3
"""Lookup fonction"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    param obj: The object to lookup
    """
    return dir(obj)
