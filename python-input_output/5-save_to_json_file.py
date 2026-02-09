#!/usr/bin/python3
"""import le module json de python"""
import json

"""function that writes an Object to a text file, using a JSON representation"""


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file"""
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
