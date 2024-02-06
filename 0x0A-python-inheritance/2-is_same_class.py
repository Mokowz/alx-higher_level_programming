#!/usr/bin/python3
"""Defines is same function"""


def is_same_class(obj, a_class):
    """True if object is exactly an instance
    Args:
        obj: object to check
        a_class: type to check
    Returns:
        boolean: True or False
    """
    return type(obj) == a_class
