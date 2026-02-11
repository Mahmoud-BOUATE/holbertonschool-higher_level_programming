#!/usr/bin/env python3

"""
Docstring for python-serialization.task_01_pickle
"""


import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """Class qui contiet le nome, age , is_student"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """fonction qui affiche les attributs"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """fonction de serialisation"""
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """fonction de déserialisation"""
        with open(filename, "rb") as f:
            obj = pickle.load(f)
        return obj
