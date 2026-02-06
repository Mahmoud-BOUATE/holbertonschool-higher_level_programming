# task_01_duck_typing.py
from abc import ABC, abstractmethod


# Classe abstraite Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        """Retourne l'aire de la forme"""
        pass

    @abstractmethod
    def perimeter(self):
        """Retourne le périmètre de la forme"""
        pass


# Classe concrète Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


# Classe concrète Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Fonction shape_info utilisant le duck typing
def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
