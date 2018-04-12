#coding:utf-8
'''
??
'''
import sympy
sympy.init_printing()
from sympy import I, pi, oo
import numpy as np

x = sympy.Symbol('x')
y = sympy.Symbol('y')
z = sympy.Symbol('z')

f = sympy.Function("f")(x)
result = f.series(x)
result = sympy.series(f, x)
x0 = sympy.Symbol("{x_0}")
result = f.series(x, x0, n = 2)
result = f.series(x, x0, n = 2).removeO()
result = sympy.cos(x).series()
result = sympy.cos(x).series(n=4)