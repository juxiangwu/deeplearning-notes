#coding:utf-8
'''
Newton法求解方程的根
'''

from matplotlib import pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
import numpy as np
import sympy

f = lambda x : np.exp(x) - 2
tol = 0.1
xk = 2

s_x = sympy.symbols('x')
s_f = sympy.exp(s_x) - 2

f = lambda x : sympy.lambdify(s_x,s_f,'numpy')(x)
fp = lambda x : sympy.lambdify(s_x,sympy.diff(s_f,s_x),'numpy')(x)

# 可视化方程求解过程

x = np.linspace(-2.1,2.1,1000)

fig,ax = plt.subplots(1,1,figsize = (12,4))
ax.plot(x,f(x))
ax.axhline(0,ls=':',color='k')

n = 0
while f(xk) > tol:
    xk_new = xk - f(xk) / fp(xk)

    ax.plot([xk, xk], [0, f(xk)], color='k', ls=':')
    ax.plot(xk,f(xk),'ko')
    ax.text(xk,-0.5,r'$x_%d$' % n,ha='center')
    ax.plot([xk,xk_new],[f(xk),0],'k-')

    xk = xk_new
    n += 1


ax.plot(xk,f(xk),'r*',markersize=15)
ax.annotate("Root approximately at %.3f" % xk,
            fontsize=14,family='serif',
            xy = (xk,f(xk)),xycoords='data',
            xytext=(-150,+50),textcoords='offset points',
            arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=-0.5'))

ax.set_title('Newton method')
ax.set_xticks([-1,0,1,2])
plt.show()