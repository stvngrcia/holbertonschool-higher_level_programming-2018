#!/usr/bin/python3
'''
    Divides matrix by a divisor
    matrix (list)
    div (division factor)
'''


def matrix_divided(matrix, div):
    '''
        divides a matrix value by a divisor
    '''
    new_matrix = []
    try:
        length = len(matrix[0])
    except:
        pass
    int_err = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = []
        if not isinstance(row, list):
            raise TypeError(int_err)
        if length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for l in row:
            if not isinstance(l, (int, float)):
                raise TypeError(int_err)
            result = round(l / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)
    return new_matrix
