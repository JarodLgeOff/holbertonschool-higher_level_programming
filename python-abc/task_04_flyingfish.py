#!/usr/bin/python3
"""Task 04: Flying Fish"""


class Fish:
    """A class representing a fish"""
    def swim(self):
        print("The fish is swimming")

    """A method to represent the habitat of the fish"""
    def habitat(self):
        print("The fish lives in water")


class FlyingFish(Fish):
    """A class representing a flying fish, which inherits from Fish"""
    def swim(self):
        print("The flying fish is swimming!")
    """A class representing a flying fish, which inherits from Fish"""
    def fly(self):
        print("The flying fish is soaring!")
    """A method to represent the habitat of the flying fish, the Fish class"""
    def habitat(self):
        print("The flying fish lives both in water and the sky!")


class Bird:
    """A class representing a bird"""
    def fly(self):
        print("The bird is flying")
    """A method to represent the habitat of the bird"""
    def habitat(self):
        print("The bird lives in the sky")
