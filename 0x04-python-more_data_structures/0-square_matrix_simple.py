#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix == None:
        return None

    new = []

    for i in range(0, len(matrix)):
        inner = matrix[i].copy()

        for j in range(0, len(matrix[i])):
            value = matrix[i][j] * matrix[i][j]

            inner[j] = value

        new.append(inner)

    return new
