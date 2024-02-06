#!/usr/bin/python3
"""Module that contains the function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file
    Args:
        filename (str, optional): name of file. Defaults to "".
        search_string (str, optional): string to search. Defaults to "".
        new_string (str, optional): string to append. Defaults to "".
    """
    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as fil:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        fil.write(s)
