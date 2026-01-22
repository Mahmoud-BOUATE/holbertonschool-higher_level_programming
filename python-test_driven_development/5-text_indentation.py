#!/usr/bin/python3
"""
5-text_indentation module
Defines a function that prints a text with indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?' and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ".?:"
    line = ""

    for char in text:
        line += char
        if char in special_chars:
            print(line.strip())
            print()
            line = ""

    if line.strip():
        print(line.strip(), end="")
