import numpy as np
def matrix_subtracton(num1, num2):
    res = np.subtract(num1, num2)
    return (str(res)).replace('[','').replace(']','')
mat1 = np.array([[10, 5, 4, 2],[5, 10, 9, 55,], [9, 19, 69, 8,], [7, 8, 4, 75]])
mat2 = np.array([[12, 65, 34, 2,], [1, 5, 8, 45,], [7, 21, 63, 8,], [0, 78, 4, 65]])
print('Martix 1:', '\n', str(mat1).replace('[','').replace(']',''))
print('Martix 2:', '\n',str(mat2).replace('[','').replace(']',''))
print('The result matrix is:', '\n' , matrix_subtracton(mat1, mat2))
