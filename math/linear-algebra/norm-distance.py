# -*- coding: utf-8 -*-
'''
标准化欧氏距离
'''

import numpy as np 

vectormat = np.mat([[1,2,3],[4,5,6]])

v12 = vectormat[0] - vectormat[1]
print(np.sqrt(v12*v12.T))

#标准化
varmat = np.std(vectormat.T,axis = 0)
normvmat = (vectormat - np.mean(vectormat)) / varmat.T 
normv12 = normvmat[0] - normvmat[1]

print(np.sqrt(normv12 * normv12.T))
