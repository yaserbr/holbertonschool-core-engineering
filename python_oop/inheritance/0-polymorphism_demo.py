#!/usr/bin/env python3
"""Module that defines the BaseGeometry class."""


class Animal:
    """Represents an animal."""
    def speak(self):
        """Returns a generic sound for the animal."""
        return "Some sound"


class Dog(Animal):
    """Represents a dog, which is a subclass of Animal."""
    def speak(self):
        """Returns the sound a dog makes."""
        return "Woof"


class Cat(Animal):
    """Represents a cat, which is a subclass of Animal."""
    def speak(self):
        return "Meow"
