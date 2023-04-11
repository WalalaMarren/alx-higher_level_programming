#!/usr/bin/python3
"""Defining new fuction to check instance of a class"""


def is_same_class(obj, a_class):
    """Function to check class instance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
