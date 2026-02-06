#!/usr/bin/env python3
"""Create an animal and its subclasses with an abstract methode"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal"""
    @abstractmethod
    def sound(self):
        """
        Abstract method for making a sound
        Must be implemented by all subclasses
        """
        pass


class Dog(Animal):
    """Concrete subclass of Animal representing a Dog"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Concrete subclass of Animal representing a Cat"""
    def sound(self):
        return "Meow"
