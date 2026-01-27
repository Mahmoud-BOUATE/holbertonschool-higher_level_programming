#!/usr/bin/python3
"""Define a class Square with size and position."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position with validation."""
        if (
            isinstance(value, tuple) and
            len(value) == 2 and
            isinstance(value[0], int) and
            isinstance(value[1], int) and
            value[0] >= 0 and
            value[1] >= 0
        ):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Return current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with # characters, respecting position."""
        if self.__size == 0:
            print()
            return

        for j in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
