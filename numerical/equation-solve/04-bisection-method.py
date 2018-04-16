#coding:utf-8
'''
Bisection法求解方程的根
'''

from matplotlib import pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
import numpy as np

f = lambda x : np.exp(x) - 2
tol = 0.1
a,b = -2,2

x = np.linspace(-2.1,2.1,1000)

fig,ax = plt.subplots(1,1,figsize = (12,4))
ax.plot(x,f(x),lw = 1.5)
ax.axhline(0,ls=':',color='k')
ax.set_xticks([-2,-1,0,1,2])
ax.set_xlabel(r'$x$',fontsize=18)
ax.set_ylabel(r'$f(x)$',fontsize=18)

fa,fb = f(a),f(b)
ax.plot(a,fa,'ko')
ax.plot(b,fb,'ko')
ax.text(a,fa+0.5,r'$a$',ha='center',fontsize=18)
ax.text(b,fb+0.5,r'$b$',ha='center',fontsize=18)

n = 1
while b - a > tol:
    m = a + (b - a) / 2
    fm = f(m)

    ax.plot(m,fm,'ko')
    ax.text(m,fm - 0.5,r'$m_%d$' %n,ha = 'center')
    n += 1

    if np.sign(fa) == np.sign(fm):
        a,fa = m,fm
    else:
        b,fb = m,fm

ax.plot(m,fm,'r*',markersize=10)
ax.annotate("Root approximately at %.3f" % m,
            fontsize=14,family='serif',
            xy = (a,fm),xycoords='data',
            xytext=(-150,+50),textcoords='offset points',
            arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=-0.5'))

ax.set_title('Bisection method')

plt.show()