#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixclone = []

    for i in range(len(matrix)):
        matrixclone.append([])
        j = 0
        while j < len(matrix[i]):
            matrixclone[i].append(matrix[i][j]**2)
            j += 1
    return matrixclone
