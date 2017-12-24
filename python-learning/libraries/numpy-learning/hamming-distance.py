# -*- coding: utf-8 -*-
'''
汉明距离
'''
import numpy as np 

matV = np.mat([[1,1,0,1,0,1,0,0,1],[0,1,1,0,0,0,1,1,1]])
smstr = np.nonzero(matV[0] - matV[1])

print(np.shape(smstr)[1])