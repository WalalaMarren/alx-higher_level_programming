#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square class that inherits from Rectangle"""

    def __init__(self, size):
        """Constructor to initialize a new square.
    Args:
        size (int): The size of the new square.
    """
    self.integer_validator("size", size)
    self.__size = size
