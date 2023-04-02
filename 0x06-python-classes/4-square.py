#!/usr/bin/python3

"""Creating a new class of Square name"""
class Square:
    """defining the class square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """getting the property of size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """public method to calculate the area"""
        return self.__size ** 2
