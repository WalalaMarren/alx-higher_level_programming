#!/usr/bin/python3
"""Defining a new subclass Rectangle"""


class Rectangle(BaseGeometry):
    """This is a new class Rectangle which is an instance of BaseGeometry"""

    def __init__(self, width, height):
        """This is a contructor method that's called every time a new obj is created
        Args:
            width: Parameter for the width, private
            height: Parameter for the height, private
        """
        self.__width = width
        self.__height = height
