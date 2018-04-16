#coding:utf-8
'''
表达式
'''
import sympy
sympy.init_printing()
from sympy import I, pi, oo

# 创建表达式
x = sympy.Symbol("x")
y = sympy.Symbol("y")
expr = 1 + 2 * x**2 + 3 * x**3
print(expr)
print(expr.args)

# 表达式简化
expr = 2 * (x**2 - x) - x * (x + 1)
print(expr)
print('simplify:',sympy.simplify(expr))
print('simplify:',expr.simplify())
expr = 2 * sympy.cos(x) * sympy.sin(x)
print(sympy.simplify(expr))
expr = sympy.exp(x) * sympy.exp(y)
print(expr.simplify())

'''
表达式简化，还可以通过调用sympy.trigsimp，sympy.powsimp，sympy.compsimp和sympy.ratsimp来简化
'''

# 表达式展开
expr = (x + 1) * (x + 2)
print('expand:',sympy.expand(expr))

# 三角函数展开
expr = sympy.sin(x + y)
print('expand:',sympy.expand(expr,trig=True))
print('expand:',expr.expand(trig=True))
expr = x*sympy.sin(x) + sympy.sin(x + y) + y
print('expand:',expr.expand(trig=True))

# 对数函数展开
a, b = sympy.symbols("a, b", positive=True)
print('expand:',sympy.log(a * b).expand(log=True))

# 复函数数展开
expr = sympy.exp(I*a + b)
print('expand:',expr.expand(complex=True))

# 幂函数展开
print('expand:',sympy.expand((a * b)**x, power_base=True))
print('expand:',sympy.exp((a-b)*x).expand(power_exp=True))

# 因式分解、合并同类项，
expr = sympy.factor(x**2 - 1)
print('factor:',expr)

# 三角函数因式分解
z = sympy.Symbol('z')
expr = sympy.factor(x * sympy.cos(y) + sympy.sin(z) * x)
print('factor:',expr)

# 对数函数合并
a = sympy.Symbol('a')
b = sympy.Symbol('b')
expr = sympy.logcombine(sympy.log(a) - sympy.log(b))
print('logcombine:',expr)

# 合并某个同类项
expr = x + y + x * y * z
print('collect x:',expr.collect(x))
print('collect y:',expr.collect(y))

# 通过apart函数简化表达式
expr = 1/(x**2 + 3*x + 2)
print('apart',sympy.apart(expr, x))

# 通过together函数简化表达式
print('together:',sympy.together(1 / (y * x + y) + 1 / (1+x)))

# 通过cancel函数简化表达式
print('cancel:',sympy.cancel(y / (y * x + y)))

# 表达式变量替换
# 将变量x替换成y
expr = (x + y).subs(x, y)
print('subs:x->y:',expr)
expr = sympy.sin(x * sympy.exp(x)).subs(x, y)
print('subs:',expr)
# 一次性替换多个变量
expr = sympy.sin(x * z).subs({z: sympy.exp(y), x: y, sympy.sin: sympy.cos})
print('subs:',expr)

# 表达式变量赋值
expr = x * y + z**2 *x
values = {x: 1.25, y: 0.4, z: 3.2}
print('subs:',expr.subs(values))