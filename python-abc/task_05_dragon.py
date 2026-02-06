#!/usr/bin/env python3
"""Multiple inheritance example with Fish, Bird and FlyingFish."""


class SwimMixin:
    """Mixin that adds swimming ability."""

    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Mixin that adds flying ability."""

    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """class that add addional methods or attributes"""
    def roar(self):
        print("The dragon roars!")
