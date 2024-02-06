#!/usr/bin/python3
''' function that returns the JSON of an object (string)
'''

import json


def to_json_string(my_obj):
    ''' module to json funct
     returns JSON representation
    '''
    return json.dumps(my_obj)
