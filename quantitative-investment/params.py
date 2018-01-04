# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from pylab import mpl 
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt
from scipy import stats

'''
参数估计
'''

SHindex = pd.read_csv('datas/qi/15/TRD_Index.csv')

Retindex = SHindex.Retindex

Retindex.hist()
mu = Retindex.mean()
sigma = Retindex.std()
x = np.arange(-0.06,0.062,0.002)

plt.plot(x,stats.norm.pdf(x,mu,sigma))
plt.show()

res = stats.t.interval(0.95,len(Retindex) - 1,mu,stats.sem(Retindex))
print('interval:',res)