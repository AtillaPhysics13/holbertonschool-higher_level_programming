#!/usr/bin/python3
"""Module for integer addition"""


def add_integer(a, b=98):
    """Adds two integers and returns their sum"""

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
