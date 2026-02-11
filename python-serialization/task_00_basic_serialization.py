#!/usr/bin/env python3
"""
Docstring for python-serialization.task_00_basic_serialization
"""
import json

def serialize_and_save_to_file(data, filename):
    filename = json.dumps(data)
    print(filename)


def load_and_deserialize(filename):
    filename = json.loads(filename)
    print(filename)
