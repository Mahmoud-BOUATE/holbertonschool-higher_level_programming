#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and saves them to a file.
Uses save_to_json_file and load_from_json_file.
"""

import sys
import importlib.util
import os

# Import save_to_json_file from 5-save_to_json_file.py
spec_save = importlib.util.spec_from_file_location(
    "save_module", "./5-save_to_json_file.py"
)
save_module = importlib.util.module_from_spec(spec_save)
spec_save.loader.exec_module(save_module)
save_to_json_file = save_module.save_to_json_file

# Import load_from_json_file from 6-load_from_json_file.py
spec_load = importlib.util.spec_from_file_location(
    "load_module", "./6-load_from_json_file.py"
)
load_module = importlib.util.module_from_spec(spec_load)
spec_load.loader.exec_module(load_module)
load_from_json_file = load_module.load_from_json_file

# File to store the list
filename = "add_item.json"

# Load existing list if file exists, else start with empty list
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add all command-line arguments (excluding script name)
items.extend(sys.argv[1:])

# Save updated list to JSON file
save_to_json_file(items, filename)
