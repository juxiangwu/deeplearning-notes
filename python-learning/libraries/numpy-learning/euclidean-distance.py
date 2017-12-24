# -*- coding: utf-8 -*-

'''
欧氏距离
distance = sqrt((vec1 - vec2) * ((vec1 - vec2).T))
'''

import numpy as np 

vec1 = np.mat([1,2,3])
vec2 = np.mat([4,5,6])

dst = np.sqrt((vec1 - vec2) * ((vec1 - vec2).T))
print(dst)