#!/usr/bin/python3
"""Defining a new subclass Rectangle"""
Rectangle = __import__('9-Rectangle').Rectangle


class Square(Rectangle):
    """class Rectangle which inherits property and methods of BaseGeometry"""

    def __init__(self, size):
        """This is a contructor to initialize new rectangle
        Args:
            size(int): Parameter for the width and height private
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return the area of the rectangle."""
        return self.__size * self.__size
