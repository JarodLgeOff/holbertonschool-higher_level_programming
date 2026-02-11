#!/usr/bin/python3

"""11. Student to JSON with reload"""


class Student:
    """Student class
        self: The instance of the Student class
        first_name: The first name of the student
        last_name: The last name of the student
        age: The age of the student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if isinstance(attrs, list) and all(isinstance(b, str) for b in attrs):
            return {key: self.__dict__[key]
                    for key in attrs if key in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance from a dictionary"""
        for key, value in json.items():
            self.__dict__[key] = value
