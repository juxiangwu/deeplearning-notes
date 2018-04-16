#coding:utf-8

'''
创建符号
'''
import sympy
sympy.init_printing()
from sympy import I, pi, oo

x = sympy.Symbol('x')
# x的类型还未确定
print('x is real:',x.is_real)

# 创建实数符号
y = sympy.Symbol('y',real=True)
print('y is real:',y.is_real)

# 创建虚数符号
z = sympy.Symbol('z',imaginary = True)
print('z is real:',z.is_real)

# 创建正数和负数符号
g = sympy.Symbol('g',positive = True)
h = sympy.Symbol('h',negative = True)
print('g is positive:',g.is_positive)
print('h is negative:',h.is_negative)

# 创建整数符号
i = sympy.Symbol('i',integer = True)
print('i is integer:',i.is_integer)

'''
还可以通过指数odd,even,prime,infinite,finite等来创建奇数，偶数等等
'''
# 创建符号表达式
expression = sympy.sqrt(x ** 2)
print(expression)


# 自动简化符号表达式
n1 = sympy.Symbol('n')
n2 = sympy.Symbol('n',integer = True)
n3 = sympy.Symbol('n',odd = True)
print(sympy.cos(n1 * pi))
print(sympy.cos(n2 * pi))
print(sympy.cos(n3 * pi))

# 一次性创建多个相同类型的符号
a, b, c = sympy.symbols("a, b, c", negative=True)