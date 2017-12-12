#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index, i in enumerate(row):
            print("{:d}".format(i), end="")
            if (index < len(row) - 1):
                print("{}".format(" "), end="")
        print()
