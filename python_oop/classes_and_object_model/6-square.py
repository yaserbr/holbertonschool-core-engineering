#!/usr/bin/env python3
"""Module that defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position attribute."""
        return self.__position
    @position.setter
    def position(self, value):
        """Setter for the position attribute."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.size * self.size

    def my_print(self):
        """Prints the square using the '#' character."""
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print("#" * self.size)
    def __str__(self):
        self.my_print()
        return ""
