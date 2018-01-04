# -*- coding:utf-8 -*-
'''
二项分布随机数
'''

import numpy as np
import pandas as pd
from pylab import mpl 
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt
from scipy import stats

y = np.random.binomial(100,0.5,100)
x = np.arange(0,100)

# 100试验，有20次正面朝上的概率值
# pmf 二项分布的概率质量函数
val = stats.binom.pmf(20,100,0.5)
print(val)

# 累积密度函数
val = stats.binom.cdf(20,100,0.5)
print(val)

#plt.plot(x,y)
#plt.show()