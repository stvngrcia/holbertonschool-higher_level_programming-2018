#!/usr/bin/python3
""" Doc """

matrix_divided = __import__('2-matrix_divided').matrix_divided

try:
    matrix = [[3, "9"], [12, 3]]
    print(matrix_divided(matrix, 2))
    print(matrix)
except Exception as e:
    print(e)

try:
    matrix = [[3, 9], [12, 3]]
    print(matrix_divided(matrix, "2"))
    print(matrix)
except Exception as e:
    print(e)