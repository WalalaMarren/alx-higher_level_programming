#!/usr/bin/python3
"""writing objects to a text file"""
import json

def save_to_json_file(my_obj, filename):
    """Function to write to a text file using JSON rep"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
