#!/usr/bin/python3
"""writing objects to a text file"""


def save_to_json_file(my_obj, filename):
    """Function to write to a text file using JSON rep"""
    with open(filename, "w", encoding="utf-8") as f:
        string = str(my_obj)
        f.write(string)
