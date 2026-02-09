#!/usr/bin/python3
"""
Student module
Defines a Student class with JSON serialization capability
"""


class Student:
    """Initialize a Student instance"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the instance"""

        return self.__dict__
