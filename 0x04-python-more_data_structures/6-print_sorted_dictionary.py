#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        sorted_keys = sorted(a_dictionary.keys())

        for keys in sorted_keys:
            print('{:s}: {}'.format(keys, sorted_keys[keys]))
