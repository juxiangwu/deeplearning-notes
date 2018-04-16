#coding:utf-8
'''
函数极限
'''
import sympy
sympy.init_printing()
from sympy import I, pi, oo
import numpy as np

x = sympy.Symbol('x')
expr = sympy.sin(x) / x
result = sympy.limit(expr,x,0)
print('limit:',result)

f = sympy.Function('f')
x, h = sympy.symbols("x, h")
diff_limit = (f(x + h) - f(x))/h
result = sympy.limit(diff_limit.subs(f, sympy.cos), h, 0)
print('limit:',result)
result = sympy.limit(diff_limit.subs(f, sympy.sin), h, 0)
print('limit:',result)

expr = (x**2 - 3*x) / (2*x - 2)
p = sympy.limit(expr/x, x, sympy.oo)
q = sympy.limit(expr - p*x, x, sympy.oo)
print('result:p,q = ',p,q)

# 求和
n = sympy.symbols("n", integer=True)
s = sympy.Sum(1/(n**2), (n, 1, oo))
print('sum:',s)
print('sum:',s.doit())

# 求积
p = sympy.Product(n, (n, 1, 7))
print('product:',p)
print('product:',p.doit())

expr = sympy.Sum((x)**n/(sympy.factorial(n)), (n, 1, oo)).doit().simplify()
print('expr:',expr)