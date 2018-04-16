#coding:utf-8
'''
微积分
'''

import sympy
sympy.init_printing()
from sympy import I, pi, oo
import numpy as np

# 1、求函数的导数
x = sympy.Symbol('x')
y = sympy.Symbol('y')
z = sympy.Symbol('z')
f = sympy.Function('f')(x)
# 对函数f的变量x进行求导
print('diff x:',sympy.diff(f, x))

# 对函数f的变量x进行求解二阶导数和三阶导数
print('diff x:',sympy.diff(f, x, x))
print('diff x:',sympy.diff(f, x, 3))

# 对函数多个变量求不同阶次的导数
g = sympy.Function('g')(x, y)
result = g.diff(x, y)
result = g.diff(x,2,y,3)

# 具体函数求导实例
expr = x**4 + x**3 + x**2 + x + 1
# 求一阶导数
result = expr.diff(x)
# 求二阶导数
result = expr.diff(x, x)

expr = (x + 1)**3 * y ** 2 * (z - 1)
result = expr.diff(x, y, z)

# 三角函数求导
expr = sympy.sin(x * y) * sympy.cos(x / 2)
result = expr.diff(x)
# 特殊函数求导
expr = sympy.special.polynomials.hermite(x, 0)
result = expr.diff(x).doit()

d = sympy.Derivative(sympy.exp(sympy.cos(x)), x)
# 通过调用doit函数执行求导
result = d.doit()

# 2、积分
a, b, x, y = sympy.symbols("a, b, x, y")
f = sympy.Function("f")(x)
# 函数的积分
result = sympy.integrate(f)
# 函数在某个期间的积分
result = sympy.integrate(f, (x, a, b))

result = sympy.integrate(sympy.sin(x))
print('result = ',result)
print('result = ',sympy.integrate(sympy.sin(x), (x, a, b)))
result = sympy.integrate(sympy.exp(-x**2), (x, 0, oo))
print('result = ',result)

# 函数从某个值到无穷期间的积分
result = sympy.integrate(sympy.exp(-x**2), (x, 0, oo))
a, b, c = sympy.symbols("a, b, c", positive=True)
result = sympy.integrate(a * sympy.exp(-((x-b)/c)**2), (x, -oo, oo))