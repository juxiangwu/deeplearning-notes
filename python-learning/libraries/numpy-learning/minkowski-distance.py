# -*- coding: utf-8 -*-
'''
闵可夫斯基距离
d12 = power(sum(power(x1k - x2k),p))
'''
import numpy as np 

A = np.array([1,2,3,4,5,6,7,8,9,10])
B = np.array([1,4,9,16,25,36,49,64,81,100])

p = 1 #曼哈顿距离

d12 = np.sum((A - B))
print('d12 = ',d12)
