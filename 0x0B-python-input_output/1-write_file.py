#!/usr/bin/python3
"""Defining a new function to write into a file"""


def write_file(filename="", text=""):
    """file function to write text to filename"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
