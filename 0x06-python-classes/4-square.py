#!/usr/bin/python3
""" module contains: class Square """


class Square:
    """
        Square: defines a square.
        Attributes:
            size (int): size of square
        Method:
            __init__: Initializes size for all instances
    """

    def __init__(self, size=0):
        """ Initialization of attributes for instances
            Args:
                size (int): size of the square.
        """
        self.size = size


    @property
    def size(self):
        """ getter function to for private attribute size"""
        return (self.__size)
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
