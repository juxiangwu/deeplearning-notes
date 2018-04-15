#coding:utf-8
'''
特征值问题
'''

from __future__ import division
from scipy import linalg as la
from scipy import optimize
import sympy
import numpy as np
sympy.init_printing()
import matplotlib.pyplot as plt

# 使用符号方式求解矩阵的特征值
eps, delta = sympy.symbols("epsilon, Delta")
H = sympy.Matrix([[eps, delta], [delta, -eps]])
eigenvalue = H.eigenvals()
results = H.eigenvects()
(eval1, _, evec1), (eval2, _, evec2) = H.eigenvects()
result = sympy.simplify(evec1[0].T * evec2[0])
print('result = ',result)

# 使用scipy求解矩阵特征值
A = np.array([[1, 3, 5], [3, 5, 3], [5, 3, 9]])
evals, evecs = la.eig(A)
eigvalues = la.eigvalsh(A)