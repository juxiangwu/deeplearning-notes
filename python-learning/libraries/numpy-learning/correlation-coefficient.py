# -*- coding: utf-8 -*-
'''
相关系数与相关距离
'''
import numpy as np 

featuremat = np.mat([[1,1,2,3,4,5,6],[1,2,1,3,5,6,6]])

#计算均值
meanval1 = np.mean(featuremat[0])
meanval2 = np.mean(featuremat[1])

#计算两列标准差
dval1 = np.std(featuremat[0])
dval2 = np.std(featuremat[1])

corref = np.mean(np.multiply(featuremat[0] - meanval1,featuremat[1] - meanval2)) / (dval1 * dval2)

print('corref:',corref)
print(np.corrcoef(featuremat))