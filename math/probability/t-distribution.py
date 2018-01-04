# -*- coding:utf-8 -*-
'''
t分布
'''

import numpy as np
import pandas as pd
from pylab import mpl 
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt
from scipy import stats

x = np.arange(-4,4.004,0.004)

plt.plot(x,stats.norm.pdf(x),label='Norm')
plt.plot(x,stats.t.pdf(x,5),label='df=5')
plt.plot(x,stats.t.pdf(x,30),label='df=30')
plt.legend()

plt.title('概率密度:t分布')
plt.show()