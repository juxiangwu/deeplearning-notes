#coding:utf-8
'''
数值估算
'''

import sympy
sympy.init_printing()
from sympy import I, pi, oo
import numpy as np

print(sympy.N(1 + pi))

# 取pi的50位小数
print(sympy.N(pi, 50))

x = sympy.Symbol('x')
# 取10位小数
value = (x + 1/pi).evalf(10)
print('value = ',value)

# 生成表达在某个范围内的值
expr = sympy.sin(pi * x * sympy.exp(x))
values = [expr.subs(x, xx).evalf(3) for xx in range(0, 10)]
print('values = ',values)

# 高性能方式估算表达式的值
expr_func = sympy.lambdify(x, expr)
print('value:',expr_func(1.0))

expr_func = sympy.lambdify(x, expr, 'numpy')
xvalues = np.arange(0, 10)
values = expr_func(xvalues)
print('values:',values)