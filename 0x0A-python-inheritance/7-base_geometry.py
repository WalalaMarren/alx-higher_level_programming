#!/usr/bin/python3
"""Class definition of BaseGeometry"""


class BaseGeometry:
    """The class above is an empty class BaseGeometry to be build on"""
    def area(self):
        """this is a public method with no args"""
        raise Exception("area() is not implemented")
    def integer_validator(kself, name, value):
        """This is the second method that validates input
        Args:
            name: This is the name value to be passed
            value: The value of the name
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
