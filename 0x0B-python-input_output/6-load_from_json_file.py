#!/usr/bin/python3
"""creating an object out of JSON file"""
import json


def load_from_json_file(filename):
    """loading a JSON file into an object"""
    with open(filename, "r", encoding="utf-8") as f:
        json.load(f)
