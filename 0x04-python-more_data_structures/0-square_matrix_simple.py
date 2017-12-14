#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    if (matrix and matrix[0] and matrix[0][0]):
        for row in matrix:
            new_matrix.append(list(map(lambda x: x * x, row)))
    return (new_matrix)
