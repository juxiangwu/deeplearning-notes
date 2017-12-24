# -*- coding: utf-8 -*-
'''
夹角余弦
'''
import numpy as np 
vec1 = np.mat([1,2,3])
vec2 = np.mat([4,7,5]).reshape((3,1))

cosVal = np.dot(vec1,vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

print('consine value:',cosVal)