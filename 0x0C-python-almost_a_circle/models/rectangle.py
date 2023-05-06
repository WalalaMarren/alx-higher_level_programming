#!/usr/bin/python3
"""definition of a new class Rectangle"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """Definind a new class that inherits from the base
        Args:
            width(int): definition of width
            height(int): definition of height
            x(int): extra attr
            y(int): extra attr
            id(int): id value
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property
    def width(self):
        """get/set the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """get/set the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height == value

    @property
    def x(self):
        """get/set extra value for the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """get/set extra value for the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
