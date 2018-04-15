#coding:utf-8

'''
线性最小二乘拟合
'''

from __future__ import division
from scipy import linalg as la
from scipy import optimize
import sympy
import numpy as np
sympy.init_printing()

import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

# 定义模型
x = np.linspace(-1,1,100)
a,b,c = 1,2,3
y_exact = a + b * x + c * x ** 2

# 模拟噪声
m = 100
X = 1 - 2 * np.random.rand(m)
Y = a + b * X + c * X ** 2 + np.random.rand(m)

# 使用最小二乘法对数据进行拟合
A = np.vstack([X ** 0,X ** 1,X ** 2])
sol,r,rank,s = la.lstsq(A.T,Y)
y_fit = sol[0] + sol[1] * x + sol[2] * x**2

# 绘制数据
fig,ax = plt.subplots(figsize = (12,4))
ax.plot(X,Y,'go',alpha = 0.5,label=u'模拟数据')
ax.plot(x, y_exact, 'k', lw=2, label='真实数据 $y = 1 + 2x + 3x^2$')
ax.plot(x, y_fit, 'b', lw=2, label=u'最小二乘法拟合')
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"$y$", fontsize=18)
ax.legend(loc=2)
plt.show()