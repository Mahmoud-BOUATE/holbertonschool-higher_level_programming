#!/usr/bin/python3
"""
Module that generates Pascal's triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]  # first element

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)  # last element
        triangle.append(row)

    return triangle
