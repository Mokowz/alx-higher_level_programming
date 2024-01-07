#!/usr/bin/python3

def max_integer(my_list=[]):
    max_int = 0
    if len(max_int) == 0:
        return None
    for i, num in enumerate(my_list):
        if i == 0 or num > max_int:
            max_int = num

    return max_int
