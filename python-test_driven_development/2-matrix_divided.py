#!/usr/bin/python3
"""
Module 2-matrix_divided
Defines the function matrix_divided which divides all elements of a matrix by a divisor.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounding to 2 decimals.

    Args:
        matrix (list of list of int/float): matrix to divide
        div (int/float): divisor

    Returns:
        list of list of floats: new matrix with each element divided by div

    Raises:
        TypeError: if matrix is not a list of lists of int/float,
                   or rows are not the same size,
                   or div is not a number
        ZeroDivisionError: if div is 0

    Examples:
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> matrix_divided([[10, 20], [30, 40]], 10)
    [[1.0, 2.0], [3.0, 4.0]]
    >>> matrix_divided([[1.5, 2.5], [3.5, 4.5]], 2)
    [[0.75, 1.25], [1.75, 2.25]]
    >>> matrix_divided([[1, 2], [3, "a"]], 2)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    >>> matrix_divided([[1, 2], [3, 4]], 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
        " of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)"
            " of integers/floats")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                " of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
    return [[round(element / div, 2) for element in row] for row in matrix]
