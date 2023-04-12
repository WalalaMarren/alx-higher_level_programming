#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a file
"""

import json
import sys
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if not path.isfile('add_item.json'):
    save_to_json_file([], 'add_item.json')

items = load_from_json_file('add_item.json')
items.extend(sys.argv[1:])
save_to_json_file(items, 'add_item.json')

