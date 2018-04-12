#coding:utf-8
'''
数据类型
'''
import sympy
sympy.init_printing()
from sympy import I, pi, oo

# 整数符号
i = sympy.Integer(19)
print('type of i:',type(i),',i is real:',i.is_real,',i is integer:',i.is_Integer,',i is odd:',i.is_odd)
print(i ** 50)

# 浮点数符号
f = sympy.Float(2.35)
# 创建指定小数位数浮点数
f1 = sympy.Float(0.3,25)
print(f1)

# 如果通过符号串转换浮点数
f2 = sympy.Float('0.3',25)
print(f2)

# 有理数符号
r = sympy.Rational(11,13)
print(r)

# 有理数符号计算
r1 = sympy.Rational(2,3)
r2 = sympy.Rational(4,5)
print(r1 * r2)
print(r1 / r2)