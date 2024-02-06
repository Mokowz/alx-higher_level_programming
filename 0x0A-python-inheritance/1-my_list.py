#!/usr/bin/python3
"""inherit from list"""


class MyList(list):
    """inherits from list
    Args:
        list: list
    """
    def print_sorted(self):
        """prints a sorted list"""
        list_ = self[:]
        list_.sort()
        print(list_)
