#!/usr/bin/env python3
"""Shaopes, ietrfaces and duck Typing"""


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * 3.14

    def perimeter(self):
        return self.radius * 3.14

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def perimeter(self):
        return (self.width + self.height) * 2

def shape_info(shape):
    print(shape.area())
    print(shape.perimeter())

c = Circle(3)
r = Rectangle(4, 5)

shape_info(c)
shape_info(r)
