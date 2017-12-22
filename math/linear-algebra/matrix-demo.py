# -*- coding: utf-8 -*-

import numpy as np 
import scipy.sparse
A = np.matrix("1,2,3;4,5,6")
print(A)
B = np.matrix([[1,2,3],[4,5,6]])
print(B)

C = np.matrix([ 
    [0,10,0,0,0], 
    [0,0,20,0,0], 
    [0,0,0,30,0], 
    [0,0,0,0,40], 
    [0,0,0,0,0]])

print(C)

D = np.mat(np.ones((3,3)))
W = np.mat(np.zeros((3,3)))

S = np.bmat('D,W;W,D')
print(S)