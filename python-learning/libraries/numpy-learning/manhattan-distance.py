# -*- coding: utf-8 -*-
'''
曼哈顿距离
'''

import numpy as np 

vec1 = np.mat([1,2,3])
vec2 = np.mat([4,5,6])

dist = np.sum(np.abs(vec1 - vec2))

print('manhattan distance:',dist)