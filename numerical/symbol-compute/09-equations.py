#coding:utf-8
'''
方程求解
'''

import sympy
sympy.init_printing()
from sympy import I, pi, oo
import numpy as np

x = sympy.Symbol("x")
y = sympy.Symbol('y')
result = sympy.solve(x**2 + 2*x - 3)
print('solve:',result)

a, b, c = sympy.symbols("a, b, c")
result = sympy.solve(a * x**2 + b * x + c, x)
print('solve:',result)

result = sympy.solve(sympy.sin(x) - sympy.cos(x), x)
print('result:',result)

result = sympy.solve(sympy.exp(x) + 2 * x, x)
print('result:',result)

result = sympy.solve(x**5 - x**2 + 1, x)
print('result:',result)

eq1 = x + 2 * y - 1
eq2 = x - y + 1
result = sympy.solve([eq1, eq2], [x, y], dict=True)
print('result:',result)

