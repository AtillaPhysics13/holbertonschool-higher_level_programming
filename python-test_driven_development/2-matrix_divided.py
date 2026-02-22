#!/usr/bin/python3
"""Module that contains matrix_divided function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div and round to 2 decimal places."""
    if type(div) is bool or not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or matrix == [] or
            any(not isinstance(row, list) or row == [] for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    if any(len(row) != row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for elem in row:
            if type(elem) is bool or not isinstance(elem, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    return [[round(elem / div, 2) for elem in row] for row in matrix]
