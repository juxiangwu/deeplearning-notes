# -*- coding: utf-8 -*-
'''
马氏距离
'''
import numpy as np 

featuremat = np.mat([[1,2,3,4,5,6,7,8],[1,3,3,3,4,5,6,8]])

convinv = np.linalg.inv(conv(featuremat))
tp = featuremat.T[0] - featuremat.T[1]

distma = np.sqrt(np.dot(np.dot(tp,convinv),tp.T))
print(distma)