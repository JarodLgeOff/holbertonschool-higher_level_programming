#!/usr/bin/pytho3
"""Task 05: Dragon"""


class SwimMixin:
    """A mixin class to provide swimming capability"""
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """A mixin class to provide flying capability"""
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A class representing a dragon, from both SwimMixin and FlyMixin"""
    def roar(self):
        print("The dragon roars!")
