#!/usr/bin/python3

def no_c(my_string):
    slist = list(my_string)
    nstring = ''

    for ch in slist:
        if ch != 'c' and ch != 'C':
            nstring += ch
    return nstring
