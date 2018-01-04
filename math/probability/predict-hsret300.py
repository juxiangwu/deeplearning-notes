# -*- coding: utf-8 -*-

'''
估算沪深300上涨概率
'''

import numpy as np
import pandas as pd
from pylab import mpl 
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt
from scipy import stats


HSRet300 = pd.read_csv('datas/qi/14/return300.csv')
ret = HSRet300.iloc[:,1]

# 上涨概率
p = len(ret[ret > 0]) / len(ret)
print(p)

# 估计10个交易日中，有6天上涨的概率
prob = stats.binom.pmf(6,10,p)
print('prob:',prob)