# -*- coding: utf-8 -*-

import numpy as np 

# n阶方阵的行列式运算
A = np.mat([[1,2,4,5,6],[9,12,11,8,2],[6,4,3,2,1],[9,1,3,4,5],[0,2,3,4,1]])
print(A)

#方阵的行列式
res = np.linalg.det(A)
print('det:\n',res)

#矩阵的逆

invA = np.linalg.inv(A)
print('inv(A):\n',invA)

#矩阵对称
AT = A.T
res = A * AT
print('A*A.T:\n',AT)

#矩阵的秩
rankVal = np.linalg.matrix_rank(A)
print('rank:\n',rankVal)

#可逆矩阵求解
b = [1,0,1,0,1]
S = np.linalg.solve(A,b)
print('solve:\n',S)
