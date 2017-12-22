# -*- coding: utf-8 -*-

import numpy as np 

A = np.array([1,2,3,4,5,6,7,8,9])
B = np.array([1,2,3,4,5,6,7,8,9])

D = np.dot(A,B)

print(D)

D2 = (A * B).sum()
print(D2)