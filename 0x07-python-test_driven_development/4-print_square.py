#!/usr/bin/python3
'''
    prints a square
    takes in the size
'''


def print_square(size):
    square = ""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for c in range(size):
        square += "#" * size + "\n"
    print(square, end="")
