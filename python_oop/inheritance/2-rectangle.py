#!/usr/bin/env python3
"""Module that defines the BaseGeometry class."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class inhareyed from basegeometry class"""
    def __init__(self, width, height):
        """init once object created"""
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns string representation of rectangle"""
        return "[Rectangle] {} / {}".format(self.__width, self.__height)
