#!/usr/bin/env python3
"""Abstract classes"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """new Abstract class"""

    @abstractmethod
    def sound(self):
        """abstract function that return the sound of the animal."""
        pass


class Dog(Animal):
    """dog class inherits from Animal"""
    def sound(self):
        """overwrite the parint function"""
        return "Bark"


class Cat(Animal):
    """cat class inherits from Animal"""
    def sound(self):
        return "Meow"
