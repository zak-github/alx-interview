#!/usr/bin/python3
"""2D MATRIX ROTATION"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D Matrix"""
    rotated = [[row[i] for row in matrix][::-1] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = rotated[i][j]
