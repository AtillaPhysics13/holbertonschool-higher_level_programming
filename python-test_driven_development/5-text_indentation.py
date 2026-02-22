#!/usr/bin/python3
"""Module that contains text_indentation function."""


def text_indentation(text):
    """Print a text with 2 new lines after each of these characters: '.', '?' and ':'.

    Args:
        text (str): input text

    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    seps = {'.', '?', ':'}
    i = 0
    # skip leading spaces for the first line
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        ch = text[i]

        if ch in seps:
            print(ch, end="")
            print("\n")
            i += 1
            # skip spaces after separator so next line doesn't start with space
            while i < len(text) and text[i] == ' ':
                i += 1
            continue

        print(ch, end="")
        i += 1
