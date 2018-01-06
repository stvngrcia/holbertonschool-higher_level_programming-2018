#!/usr/bin/python3
'''
    This module multiplies two matrices
'''


def matrix_mul(m_a, m_b):
    '''
        multipliying matrix m_a by matrix m_b
    '''
    new_matrix = []
    matrices_check(m_a, m_b)

    for a_list in m_a:
        tmp_list = [0] * (len(a_list))
        for idx, n in enumerate(a_list):
            try:
                for idp, p in enumerate(m_b[idx]):
                        tmp_list[idp] += n * p
            except Exception:
                raise ValueError("m_a and m_b can't be multiplied")
        new_matrix.append(tmp_list)
    return new_matrix


def matrices_check(m_a, m_b):
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    row_size = len(m_a[0])
    for row in m_a:
        if len(row) != row_size:
            raise TypeError("each row of m_a must should be of the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    row_size = len(m_b[0])
    for row in m_b:
        if len(row) != row_size:
            raise TypeError("each row of m_b must should be of the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
