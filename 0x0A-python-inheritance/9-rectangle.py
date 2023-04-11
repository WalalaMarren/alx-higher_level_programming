#!/usr/bin/python3
"""Defining a new subclass Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle which inherits property and methods of BaseGeometry"""

    def __init__(self, width, height):
        """This is a contructor to initialize new rectangle
        Args:
            width(int): Parameter for the width, private
            height(int): Parameter for the height, private
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
