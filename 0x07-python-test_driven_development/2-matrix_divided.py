#!/usr/bin/python3
"""
This module is composed by a function that divides the numbers of a matrix
"""


def matrix_divided(matrix, div):

    """ matrix is list of integers or floats
        div is the number in matrix
    """
    errmsg = ("matrix must be a matrix (list of lists) of integers/floats")
    errmsg2 = ("Each row of the matrix must have the same size")
    matrix = []
    for row in matrix:
        
        if len(row) != len(matrix[0]):
                raise TypeError(errmsg2)

        if not isinstance(matrix, list):
            raise TypeError(errmsg)
        
        if not all(isinstance(matrix,int, float)):
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
    
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
