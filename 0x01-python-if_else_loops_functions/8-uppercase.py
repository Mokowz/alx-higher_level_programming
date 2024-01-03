#!/usr/bin/python3

def uppercase(str):
    str1 = ''
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            str1 += chr(ord(c) - 32)
        else:
            str1 += c
    print("{}".format(str1))
