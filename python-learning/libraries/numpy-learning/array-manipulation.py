# -*- coding: utf-8 -*-

import numpy as np 
B = np.ones((3,3))
checker2by2 = np.zeros((6,6))
checker2by2[0:3,0:3] = checker2by2[3:6,3:6] = B
print(checker2by2)

a = np.array([-np.pi,np.pi])
b = np.vstack((a,np.sin(a)))
print(b)

A = np.array([5,1,1,2,1,1,2,2,10,3,3,4,5])
AA = np.unique(A)
print(AA)
BA = np.bincount(A)
print(BA)

C = np.fromfunction((lambda i,j:(i + 1) * (-1) ** (i*j)),(4,4))
print(C)