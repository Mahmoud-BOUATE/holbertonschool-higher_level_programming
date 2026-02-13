#!/usr/bin/env python3
"""
Docstring for python-serialization.task_03_xml
"""


import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Docstring for serialize_to_xml

    :param dictionary: Description
    :param filename: Description
    """

    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    Docstring for deserialize_from_xml

    :param filename: Description
    """

    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
