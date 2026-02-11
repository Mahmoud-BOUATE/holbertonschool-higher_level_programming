#!/usr/bin/env python3
"""
Docstring for python-serialization.task_00_basic_serialization
"""
import json

def serialize_and_save_to_file(data, filename):
    """fonction de serialisation"""
    filename = json.dumps(data)
    print(filename)


def load_and_deserialize(filename):
    """fonction de déserialisation"""
    data = json.loads(filename)
    print(filename)
