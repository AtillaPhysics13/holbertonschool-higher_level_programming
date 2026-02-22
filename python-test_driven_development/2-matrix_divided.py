#!/usr/bin/python3
"""Module that contains matrix_divided function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div and round results to 2 decimals.

    Args:
        matrix (list of lists): matrix of integers/floats
        div (int/float): divisor

    Returns:
        list of lists: new matrix with divided values (rounded to 2 decimals)
    """
    if (not isinstance(matrix, list) or matrix == [] or
            any(not isinstance(row, list) or row == [] for row in matrix) or
            any(not isinstance(elem, (int, float)) for row in matrix for elem in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    if any(len(row) != row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or type(div) is bool:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
