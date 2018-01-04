# -*- coding:utf-8 -*-
'''
区间估计
'''

import numpy as np
import pandas as pd
from pylab import mpl 
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt
from scipy import stats

x = [10.1,10,9.8,10.5,9.7,10.1,9.9,10.2,10.3,9.9]

# 求均值
print('mean:',np.mean(x))
# 均值的标准误差
print('sem:',stats.sem(x))

#样本均值服务t分布
res = stats.t.interval(0.95,len(x)-1,np.mean(x),stats.sem(x))
print('interval:',res)
