# -*- coding: utf-8 -*-
'''
矩阵的特征值和特征向量求解
'''
import numpy as np

A = [[1,2,3],[4,5,6],[7,8,9]]

evals,evecs = np.linalg.eig(A)

print('evals:\n',evals)
print('evecs:\n',evecs)