# -*- coding:utf-8 -*-
'''
卡方分布
'''

import numpy as np
import pandas as pd
from pylab import mpl 
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt
from scipy import stats

plt.plot(np.arange(0,5,0.02),stats.chi.pdf(np.arange(0,5,0.02),3))
plt.title('概率密度:卡方分布')
plt.show()