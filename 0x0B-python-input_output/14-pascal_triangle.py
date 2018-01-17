#!/usr/bin/python3


def pascal_triangle(n):
    '''
        Creates a pascal triangle
        Returns: A matrix containing intergers representing
                 the pascal triangle of n
    '''
    matrix = []
    for row in range(n):
        tmp_list = [0] * (row + 1)
        tmp_list[0] = 1
        tmp_list[row] = 1
        if row > 1:
            tmp_list[1] = row
            tmp_list[row - 1] = row
        # Getting the position where 0 still exist
        while 0 in tmp_list:
            idx = tmp_list.index(0)
            num = matrix[row - 1][idx] + matrix[row - 1][idx - 1]
            tmp_list[idx] = num

        matrix.append(tmp_list)
    return matrix
