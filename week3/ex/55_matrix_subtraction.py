import numpy as np

def matrix_addition (matrix1, matrix2):
    res = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
    print(matrix1)
    print(matrix2)

    for i in range(len(matrix1)):
        for j in range(len(matrix2)):
            res = matrix1[i][j] - matrix2[i][j]
            print(res)


matrix_addition([[10, 5, 4, 2,],
                 [5, 10, 9, 55],
                 [9, 19, 69, 8],
                 [7, 8, 4, 75]],
                [[12, 65, 34, 2],
                 [1, 5, 8, 45],
                 [7, 21, 63, 8],
                 [0, 78, 4, 65]])