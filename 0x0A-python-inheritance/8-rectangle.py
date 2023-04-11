#!/usr/bin/python3
"""Defining a new subclass Rectangle"""


class Rectangle(BaseGeometry):
    """This is a new class Rectangle which inherits property and methods of BaseGeometry"""

    def __init__(self, width, height):
        """This is a contructor to initialize new rectangle

        Args:
            width(int): Parameter for the width, private
            height(int): Parameter for the height, private
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
