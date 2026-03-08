#!/usr/bin/python3
"""Module that defines a function to read a file and print its content."""


def write_file(filename="", text=""):
    """Writes a string to a text file."""
    with open(filename, 'w') as f:
        f.write(text)
        return len(text)
