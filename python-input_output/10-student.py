#!/usr/bin/python3
"""
Student module
Defines a Student class with JSON serialization capability
"""


class Student:
    """ Student class """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance

        Args:
            first_name (str): student's first name
            last_name (str): student's last name
            age (int): student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of the instance.

        """

        # If attrs is a valid list of strings → filter
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            result = {}
            for key in attrs:
                if key in self.__dict__:
                    result[key] = self.__dict__[key]
            return result

        # Otherwise → return everything
        return self.__dict__
