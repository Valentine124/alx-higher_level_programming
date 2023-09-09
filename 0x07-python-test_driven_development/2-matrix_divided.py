#!/usr/bin/python3
"""
This module contains a simple function that
add a number to all element of a matrix
"""


def matrix_divided(matrix, div):
    """
    The function takes a list of list of integers and
    floats and return a new list of integer.

    Args:
        matrix - The list of list of integers
        div - The divisod

    Return:
        A new matrix with the sum of all the elements
        of matrix amd div
        An error will be raised if error occurs
    """

    if matrix is None or div is None:
        return None

    new_mat = []

    for row in matrix:
        if not (type(row) is list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        size = len(matrix[0])
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []

        for el in row:
            if not (type(div) is int) and not (type(div) is float):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")

            num = round(el / div, 2)
            new_row.append(num)

        new_mat.append(new_row)

    return new_mat
