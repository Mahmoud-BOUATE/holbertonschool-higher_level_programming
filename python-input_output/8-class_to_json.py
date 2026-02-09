#!/usr/bin/python3
""" Function that returns the dictionary description of an object for JSON serialization
"""

def class_to_json(obj):
    """Return a dictionary of all attributes of obj"""
    return obj.__dict__
