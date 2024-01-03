#!/usr/bin/python3

numb = 0

for i in range(122, 96, -1):
    if i % 2 == 0:
        numb = i
    else:
        numb = i - 32
    print("{}".format(chr(numb)), end='')
