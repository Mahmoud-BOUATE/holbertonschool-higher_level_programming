#!/usr/bin/python3
class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the instance.
        If attrs is a list of strings, only those attributes are returned.
        Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            new_dict = {}
            for key in attrs:
                if hasattr(self, key):
                    new_dict[key] = getattr(self, key)
            return new_dict

        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the instance using the dictionary json
        """
        for key, value in json.items():
            setattr(self, key, value)
