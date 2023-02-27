#!/usr/bin/python3
"""
This module is composed by a function that divides the numbers of a matrix
"""


def matrix_divided(matrix, div):

    """ matrix is list of integers or floats
        div is the number in matrix
    """
    if not isinstance(matrix, list):
        errmsg = ("matrix must be a matrix(list of list) of integers/floats")
        raise TypeError(errmsg)
    """
        matrix must be a list of lists
    """
    if matrix == [[],[]]:
        raise TypeError(errmsg)

    """
    div must be an int or float
    """
    if not isinstance(div, float, int):
        raise TypeError("div must be a number")
    """
       div cannot be equal to 0
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    """
        each row of a matrix must be the same size
    """
    for element in matrix:
        if element != len(element):
            raise TypeError("Each row of the matrix must have the same size")
    """
      All elements of the matrix should be divided by div,rounded to 2dp
    """
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
