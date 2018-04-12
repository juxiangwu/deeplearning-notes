#coding:utf-8
'''
函数
'''
import sympy
sympy.init_printing()
from sympy import I, pi, oo

x, y, z = sympy.symbols("x, y, z")
# 创建函数符号
f = sympy.Function('f')
fx = f(x)
print(fx)
g = sympy.Function('g')(x,y,z)
print(g)
print(g.free_symbols)

# 常用函数符号
sinx = sympy.sin(x)
print(sinx)
# 函数简单计算
print(sympy.sin(1.5 * pi))

# 指定函数变量的数据类型
n = sympy.Symbol('n',integer=True)
print(sympy.sin(n * pi))

# Lambda
h = sympy.Lambda(x, x**2)
print(h)
print(h(5))
print(h(1 + x))