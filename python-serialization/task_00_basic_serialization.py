#!/usr/bin/python3

"""Task 00: serialize_and_save_to_file  functions"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes data to a JSON file"""
    with open(filename, 'w') as file:
        json.dump(data, file)


"""Task 00: load_and_deserialize function"""


def load_and_deserialize(filename):
    """Deserializes data from a JSON file"""
    with open(filename, 'r') as file:
        return json.load(file)
