#!/usr/bin/python3

"""Creating a new class of Square name"""
class Square:
    """defining the class square"""
    def __init__(self, size=0):
        self.__size = size

    """setting the property of size"""
    @property
    def size(self):
        return self.__size
    """Setting the values of the attr size"""
    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """public method to calculate the area"""
        return self.__size ** 2
