#!/usr/bin/env python3
"""Module that demonstrates multiple inheritance with FlyingFish."""


class Fish:
    """Fish class"""
    def swim(self):
        """Swim fish"""
        print("The fish is swimming")

    def habitat(self):
        """habitat """
        print("The fish lives in water")


class Bird:
    """Bird"""
    def fly(self):
        """Birds fly"""
        print("The bird is flying")

    def habitat(self):
        """Habitat"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """child class"""
    def fly(self):
        """Override"""
        print("The flying fish is soaring!")

    def swim(self):
        """Override"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Habitat override"""
        print("The flying fish lives both in water and the sky!")
