#!/usr/bin/python3
"""Defining a new function to write into a file"""


def write_file(filename="", text=""):
    """This is the function to write the string"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
