# -*- coding: utf-8 -*-

import numpy as np 
import scipy.linalg

mu = 1 / np.sqrt(2)
A = np.matrix([[mu,0,mu],[0,1,0],[mu,0,-mu]])
B = scipy.linalg.kron(A,A)

print(B)

C = np.matrix('1,1j;21,3')
print(C)
print(A*A)
print(A**2)

a = np.arange(0,2 * np.pi,1.6)
D = scipy.linalg.toeplitz(a)
print(D)
print(np.exp(D))

# perform expm operation on matrix D

print(scipy.linalg.expm(D)) 

x = 10 ** 100
y = 9
v = np.matrix([x,y])
res = scipy.linalg.norm(v,2)
print(res)
