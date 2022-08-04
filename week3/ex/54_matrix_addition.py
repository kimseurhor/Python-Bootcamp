def matrix_addition (matrix1, matrix2):
    res = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
    print(matrix1)
    print(matrix2)

    for i in range(len(matrix1)):
        for j in range(len(matrix2)):
            res = matrix1[i][j] + matrix2[i][j]
            print(res)


matrix_addition([[10, 5, 4, 2],
                 [5, 0, 9, 5],
                 [9, 19, 60, 8,],
                [7, 8, 4, 5]],
                [[12, 65, 34, 42],
                 [10, 5, 89, 45],
                 [11, 21, 63, 78],
                 [87, 78, 54, 65]])
