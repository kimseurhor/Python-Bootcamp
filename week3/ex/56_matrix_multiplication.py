import numpy as np
def matrix_multiplication(num1, num2):
    if num1.shape== num2.shape:
        res = np.dot(num1, num2)
        return (str(res)).replace('[','').replace(']','')
    else:
        return ('wrong')
mat1 = np.array([[3, 7, 5], [2, 6, 7], [4, 3, 2]])
mat2 = np.array([[6, 5, 4], [3, 2, 1,], [1, 2, 3]])
print('Martix 1:', '\n', str(mat1).replace('[','').replace(']',''))
print('Martix 2:', '\n', str(mat2).replace('[','').replace(']',''))
print('The result matrix is:', '\n' , matrix_multiplication(mat1, mat2))
