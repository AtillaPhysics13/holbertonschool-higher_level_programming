#!/usr/bin/python3
"""Module that defines a function to append text."""


def append_write(filename="", text=""):
    """ appends a string to a text file."""
    with open(filename, 'a') as f:
        f.write(text)
        return len(text)
