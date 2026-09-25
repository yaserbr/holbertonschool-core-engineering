#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class"""

    @abstractmethod
    def area(self):
        """Abstract function that retearved area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract function"""
        pass


def shape_info(Shape):
    """Accepts an object of type Shape and prints its area and perimeter."""
    print("Area: {}".format(Shape.area()))
    print("perimeter: {}".format(Shape.perimeter()))


class Circle(Shape):
    """class that inherits shape"""
    def __init__(self, radius=0):
        """constroctor"""
        self.radius = radius

    def area(self):
        """Overwrite area function"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Overwrite perimeter function"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """class that inherits shape"""
    def __init__(self, width=0, height=0):
        """Constrctor"""
        self.height = height
        self.width = width

    def area(self):
        """Overwrite"""
        return self.width * self.height

    def perimeter(self):
        """Overwrite"""
        return (self.width + self.height) * 2
