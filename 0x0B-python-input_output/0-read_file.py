#!/usr/bin/python3
"""Defining a new function"""


def read_file(filename=""):
    """This is a function to read file content"""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end='')
