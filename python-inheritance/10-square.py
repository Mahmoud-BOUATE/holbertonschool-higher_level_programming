#!/usr/bin/python3
"""
Module that defines a BaseGeometry class and a Rectangle subclass
"""


class BaseGeometry:
    """Base class for geometry"""

    def area(self):
        """Raises an exception because area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer > 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry"""

    def __init__(self, width, height):
        # Valider les valeurs avant de les stocker
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        # Attributs privés
        self.__width = width
        self.__height = height

    def area(self):
        """Calculer l'aire du rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Représentation en chaîne du rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize square with validated size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return area of the square"""
        return self.__size * self.__size
