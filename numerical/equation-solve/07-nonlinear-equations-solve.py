#coding:utf-8
'''
多变量非线性方程求解
'''

import sympy
import scipy
from scipy import optimize
import numpy as np

from matplotlib import pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

'''
y - x^3 - 2*x^2 + 1 = 0
y + x^2 - 1 = 0
'''

def f(x):
    return [x[1] - x[0] ** 3 - 2 * x[0] ** 2 + 1,x[1] + x[0] ** 2 - 1]

result = optimize.fsolve(f,[1,1])
print('result = ',result)

# 使用符号方式求解
x, y = sympy.symbols("x, y")
f_mat = sympy.Matrix([y - x**3 -2*x**2 + 1, y + x**2 - 1])

# 求解雅可比矩阵
result = f_mat.jacobian(sympy.Matrix([x, y]))
print('result = ',result)

def f_jacobian(x):
    return [[-3*x[0]**2-4*x[0], 1], [2*x[0], 1]]

result = optimize.fsolve(f, [1, 1], fprime=f_jacobian)
print('result = ',result)

# 可视化求解过程
x = np.linspace(-3, 2, 5000)
y1 = x**3 + 2 * x**2 -1
y2 = -x**2 + 1

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y1, 'b', lw=1.5, label=r'$y = x^3 + 2x^2 - 1$')
ax.plot(x, y2, 'g', lw=1.5, label=r'$y = -x^2 + 1$')
x_guesses = [[-2, 2], [1, -1], [-2, -5]]

for x_guess in x_guesses:
    sol = optimize.fsolve(f, x_guess)
    ax.plot(sol[0], sol[1], 'r*', markersize=15)
    ax.plot(x_guess[0], x_guess[1], 'ko')
    ax.annotate("", xy=(sol[0], sol[1]), xytext=(x_guess[0], x_guess[1]),
        arrowprops=dict(arrowstyle="->", linewidth=2.5))
ax.legend(loc=0)
ax.set_xlabel(r'$x$', fontsize=18)

plt.show()