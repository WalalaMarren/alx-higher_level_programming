#!/usr/bin/python3
"""Function to append to a text file"""


def append_write(filename="", text=""):
    """appends to a file filename the text content"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
