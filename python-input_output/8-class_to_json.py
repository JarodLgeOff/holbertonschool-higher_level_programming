#!/usr/bin/python3
"""8. Class to JSON"""


def class_to_json(obj):
    """Returns dict description of object for JSON serialization"""
    return obj.__dict__
