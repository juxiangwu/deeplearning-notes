#coding:utf-8
'''
求解线性方程组
'''
from __future__ import division
from scipy import linalg as la
from scipy import optimize
import sympy
import numpy as np
sympy.init_printing()
import matplotlib.pyplot as plt

'''
求解线性方程组
2x1 + 3x2 = 4
5x1 + 4x2 = 3
'''

# 使用符号方式求解
A = sympy.Matrix([[2,3],[5,4]])
b = sympy.Matrix([4,3])

print('rank:',A.rank())
print('condition number:',A.condition_number())
print('A.norm():',A.norm())

# LU分解
L, U, _ = A.LUdecomposition()
print('L,U = ',L,U)
print('L * U = ',(L * U)) # equivalent to A.LUsolve(b)
x = A.solve(b)
print('x = ',x)

# 使用scipy线性库求解
A = np.array([[2, 3], [5, 4]])
b = np.array([4, 3])
print('rank:',np.linalg.matrix_rank(A))
print('cond:',np.linalg.cond(A))

# LU分解
P, L, U = la.lu(A)
print('L,U = ',L,U)
print('L * U = ',L * U)
x = la.solve(A,b)
print('x = ',x)

