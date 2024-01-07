#!/usr/bin/python3
"""Defines a matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices
    Args:
        m_a (list of lists): First matrix
        m_b (list of lists): Second matrix
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    n_col1 = 0
    n_row2 = 0

    if m_a == []:
        raise ValueError("m_a can't be empty")
    for row1 in m_a:
        if type(row1) != list:
            raise TypeError("m_a must be a list of lists")
        len1 = len(m_a[0])
        if row1 == []:
            raise ValueError("m_a can't be empty")
        if len1 != len(row1):
            raise TypeError("each row of m_a must be of the same size")
        n_col1 = len(row1)
        for column1 in row1:
            if type(column1) != int and type(column1) != float:
                raise TypeError("m_a should contain only integers or floats")

    if m_b == []:
        raise ValueError("m_b can't be empty")
    for row2 in m_b:
        if type(row2) != list:
            raise TypeError("m_b must be a list of lists")
        len2 = len(m_b[0])
        if row2 == []:
            raise ValueError("m_b can't be empty")
        if len2 != len(row2):
            raise TypeError("each row of m_b must be of the same size")
        n_row2 += 1
        for column2 in row2:
            if type(column2) != int and type(column2) != float:
                raise TypeError("m_b should contain only integers or floats")

    if n_col1 != n_row2:
        raise ValueError("m_a and m_b can't be multiplied")

    mul_matrix = []

    for row_1 in m_a:
        l = 0
        l_row = []
        while l < len(m_b[0]):
            result = 0
            k = 0
            for column_1 in row_1:
                result += column_1 * m_b[k][l]
                k += 1
            l_row.append(result)
            l += 1
        mul_matrix.append(l_row)

    return mul_matrix
