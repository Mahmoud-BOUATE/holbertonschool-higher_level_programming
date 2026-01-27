#!/usr/bin/python3
"""Define a class rectangle."""


class Rectangle:
    """Represent a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width."""
        return self.__width

    @width.setter
    def width(self, value):
        """set width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve width."""
        return self.__height

    @height.setter
    def height(self, value):
        """set width with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """return the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle represented with '#' characters."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_rows = []
        for i in range(self.__height):
            rectangle_rows.append("#" * self.__width)
        return "\n".join(rectangle_rows)

    def my_print(self):
        """Print the rectangle using '#' characters."""
        print(self.__str__())

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"
