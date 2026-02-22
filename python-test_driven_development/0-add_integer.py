#!/usr/bin/python3
"""Module that contains add_integer function."""
def add_integer(a, b=98):
    """Add 2 integers.
    a and b must be integers or floats, otherwise raise TypeError.
    Floats are casted to integers before addition.

    Returns:
        int: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
