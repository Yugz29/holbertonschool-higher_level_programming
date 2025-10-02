#!/usr/bin/python3
"""
This script adds all command line arguments to a Python list stored
in a JSON file.
"""
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""
Load the current list from 'add_item.json' if it exists, otherwise start with
an empty list.
Append all command line arguments (excluding the script name) to this list.
Save the updated list back to 'add_item.json'.
"""
try:
    arglist = load_from_json_file("add_item.json")
except FileNotFoundError:
    arglist = []

arglist.extend(argv[1:])
save_to_json_file(arglist, "add_item.json")
