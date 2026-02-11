#!/usr/bin/env python3
"""
Docstring for python-serialization.task_00_basic_serialization
"""
import json

def serialize_and_save_to_file(data, filename):
    """fonction de serialisation"""
    with open("filename", "w") as f:
        json.dump(data,f)


def load_and_deserialize(filename):
    """fonction de déserialisation"""
    with open(filename, "r") as f:
        return json.load(f)
