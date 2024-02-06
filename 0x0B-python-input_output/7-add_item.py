#!/usr/bin/python3
"""Module that loads, adds and saves arguments to a Python list"""
from sys import argv


load_file = __import__('6-load_from_json_file').load_from_json_file
save_file = __import__('5-save_to_json_file').save_to_json_file

try:
    lst = load_file('add_item.json')
except (ValueError, FileNotFoundError):
    lst = []

for item in argv[1:]:
    lst.append(item)

save_file(lst, 'add_item.json')
