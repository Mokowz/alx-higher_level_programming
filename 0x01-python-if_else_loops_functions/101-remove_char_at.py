#!/usr/bin/python3

def remove_char_at(str, n):
    new_str = ''
    for i in range(len(str)):
        if i == n:
            new_str[i] = ''
        else:
            new_str[i] = str[i]

    return new_str
