#!/usr/bin/python3
"""
print squares
"""


def print_square(size):
    """Prints a square with # representing dimensions
    Arguments:
        size (int): size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size > 0:
        for i in range(size):
            print("#" * size)
