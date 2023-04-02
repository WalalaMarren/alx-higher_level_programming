#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    try:
        def __init__(self, size=0):
            self.__size = size
    except TypeError:
        print("size must be an integer")
    except ValueError:
        print("size must be >= 0")
