#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
