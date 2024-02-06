#!/usr/bin/python3
'''Defines a  function that writes an Object to a text file
'''
import json


def save_to_json_file(my_obj, filename):
    ''' module save_to_json
    '''
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
