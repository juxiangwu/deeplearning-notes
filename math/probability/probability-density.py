# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from pylab import mpl 
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt
from scipy import stats


HSRet300 = pd.read_csv('datas/qi/14/return300.csv')
res = HSRet300.head(n=2)
print(res)

density = stats.kde.gaussian_kde(HSRet300.iloc[:,1])
bins = np.arange(-5,5,0.02)

plt.subplot(211)
plt.plot(bins,density(bins))
plt.title('沪深300收益率序列的概率密度曲线')
plt.subplot(212)
plt.plot(bins,density(bins).cumsum())
plt.title('沪深300收益率序列的累积分布函数图')
plt.show()