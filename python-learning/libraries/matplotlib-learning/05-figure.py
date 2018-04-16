#coding:utf-8
'''
Matplotlib Figure
'''

import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(figsize=(8,2.5),facecolor='#f1f1f1')

# 坐标轴
left,bottom,width,height = 0.1,0.1,0.8,0.8
ax = fig.add_axes((left,bottom,width,height),facecolor='#e1e1e1')

x = np.linspace(-2,2,1000)
y1 = np.cos(40 * x)
y2 = np.exp(-x ** 2)

ax.plot(x,y1 * y2)
ax.plot(x,y2,'g')
ax.plot(x,-y2,'g')
ax.set_xlabel('x')
ax.set_ylabel('y')

fig.savefig('datas/graph.png')
