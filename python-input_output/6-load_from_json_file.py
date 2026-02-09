#!/usr/bin/python3
"""import le module json de python"""
import json

"""function that creates an Object from a "JSON file"""


def load_from_json_file(filename):
    """create an Object from JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)
