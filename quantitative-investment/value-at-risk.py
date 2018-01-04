# -*- coding:utf-8 -*-
'''
正态分布在金融市场的应用：VaR(Value at Risk)指的是在一定概率水平(a%)下，
某一金融资产或金融资产组合在未来特定的一段时间内的最大可能损失。
'''

import numpy as np
import pandas as pd
from pylab import mpl 
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt
from scipy import stats

HSRet300 = pd.read_csv('datas/qi/14/return300.csv')
ret = HSRet300.iloc[:,1]

# 沪深300收益率序列均值
HS300_RetMean = ret.mean()

print('mean:',HS300_RetMean)

# 沪深300收益率方差
HS300_RetVariance = ret.var()
print('variance:',HS300_RetVariance)

# 查询累积密度值为0.05的分位数，表示超过95%的概率损失不会超过分位数的数值
res = stats.norm.ppf(0.05,HS300_RetMean,HS300_RetVariance ** 0.5)
print('ppf:',res)