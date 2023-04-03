#!/usr/bin/python3
"""defining a class rectangle"""


class Rectangle:
    """
    defining the class rectangle
    Args:
        width : must be an integer
        height: must be an integer
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        This is a method that retrives the width value.
        it takes no arguments besides the reference parameter.the setter is used to set the attributes
        """
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """
        This is a method that retrives the width value.
        it takes no arguments besides the reference parameter.the setter is used to set the attributes
        """
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
