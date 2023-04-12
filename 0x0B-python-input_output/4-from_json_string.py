#!/usr/bin/python3
"""Function to deserialize JSON data to an onj"""
import json


def from_json_string(my_str):
    """This is a function to deserialize my_str"""
    return json.loads(my_str)
