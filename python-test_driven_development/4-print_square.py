#!/usr/bin/python3
"""Module that contains print_square function."""


def print_square(size):
    """Print a square of size `size` using the character #.

    Args:
        size (int): length of the square side

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is < 0
    """
    # If size is a float (even 3.0), it must raise TypeError per spec
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
