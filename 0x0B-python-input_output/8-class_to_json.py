#!/usr/bin/python3
'''Defines a function that returns the dictionary description
'''


def class_to_json(obj):
    '''module class_to_json
       returns builds a dictionary
    '''
    return obj.__dict__
