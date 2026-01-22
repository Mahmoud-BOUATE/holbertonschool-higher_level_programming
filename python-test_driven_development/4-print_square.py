#!/usr/bin/python3
"""
4-print_square module
Defines a function that prints a square using '#'.
"""


def print_square(size):
    """
    Prints a square of size `size` with the character '#'.
    """
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
