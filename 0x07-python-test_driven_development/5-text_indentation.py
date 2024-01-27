#!/usr/bin/python3


def text_indentation(text):
    """Prints two new lines after
    characters: to separate the words
    Args:
        text (str): string text
    Raises:
        TypeError: if `text` is not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    strin =  ''
    j = 0
    while j < len(text):
        strin += text[j]
        if text[j] in ['.', '?', ':']:
            strin = strin.strip()
            print(strin + '\n')
            try:
                if text[j + 1] == ' ':
                    j += 1
            except IndexError:
                pass
            strin = ''
        j += 1

    if len(strin) > 0:
        print(strig, end="")
