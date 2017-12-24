# -*- coding: utf-8 -*-
'''
杰卡德相似系数
'''
import numpy as np 
import scipy.spatial.distance as dist

matV = np.mat([[1,1,0,1,0,1,0,0,1],[0,1,1,0,0,0,1,1,1]])
print('dist.jaccard:',dist.pdist(matV,'jaccard'))
