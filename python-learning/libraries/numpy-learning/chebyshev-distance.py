# -*- coding: utf-8 -*-

'''
切比雪夫距离
'''

import numpy as np 
vec1 = np.mat([1,2,3])
vec2 = np.mat([4,7,5])

dist = np.abs(vec1 - vec2).max()

print('chebyshev distance:',dist)