#!/usr/bin/python3
"""Return lookup"""


def lookup(obj):
    """ returns list of attributes
    Args:
        obj (object): object
    """
    return dir(obj)
