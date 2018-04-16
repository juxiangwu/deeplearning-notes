#coding:utf-8
'''
线性代数
'''
import sympy
sympy.init_printing()
from sympy import I, pi, oo
import numpy as np

# 创建矩阵
A = sympy.Matrix([1,2])
B = sympy.Matrix([[1,2]])
C = sympy.Matrix(3, 4, lambda m, n: 10 * m + n)
print('A = ',A)
print('b = ',B)
print('C = ',C)

a, b, c, d = sympy.symbols("a, b, c, d")
M = sympy.Matrix([[a, b], [c, d]])
print('M = ',M)
print('M * M = ',M * M)

x = sympy.Matrix(sympy.symbols("x_1, x_2"))
print('x = ',x)
print('M * x = ',M * x)

# 线性方程组求解
'''
x + p y = b1 ,
q x + y = b2,
'''
p, q = sympy.symbols("p, q")
M = sympy.Matrix([[1, p], [q, 1]])
print('M = ',M)
b = sympy.Matrix(sympy.symbols("b_1, b_2"))

x = M.LUsolve(b)
print('x = ',x)


x = M.inv() * b
print('x = ',x)