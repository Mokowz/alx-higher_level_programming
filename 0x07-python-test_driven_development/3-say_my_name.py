#!/usr/bin/python3

""" say_my_name

Prints My name is `first_name` `last_name`
"""


def say_my_name(first_name, last_name=""):
    """ add_integer - prints first and last name

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print('My name is {:s} {:s}'.format(first_name, last_name))
