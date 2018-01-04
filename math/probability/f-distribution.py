# -*- coding:utf-8 -*-
'''
F分布
'''

import numpy as np
import pandas as pd
from pylab import mpl 
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt
from scipy import stats

x = np.arange(0,5,0.002)

plt.plot(x,stats.f.pdf(x,4,40))
plt.title('概率密度:F分布')
plt.show()