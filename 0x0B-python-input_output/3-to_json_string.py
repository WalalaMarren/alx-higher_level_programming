#!/usr/bin/python3
"""Introducing the JSON file serialization"""
import json


def to_json_string(my_obj):
    """Function to return the JSON format of my_obj"""
    return json.dumps(my_obj)
