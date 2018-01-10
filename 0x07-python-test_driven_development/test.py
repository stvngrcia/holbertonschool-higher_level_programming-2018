#!/usr/bin/python3
""" Doc """

def matrix_divided(matrix, div):
    """ Doc """
    if div == float('inf') or div == -float('inf') or div != div:
        div = 10
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or (len(matrix) == 0) or type(matrix[0]) is not list or (len(matrix[0]) == 0):
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for c in row:
            if type(c) is not int and type(c) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    return [[round(item / div, 2) for item in row] for row in matrix]