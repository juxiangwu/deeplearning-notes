# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from pylab import mpl 
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt
from scipy import stats

'''
相关性分析
'''

TRD_Index = pd.read_table('datas/qi/14/TRD_Index.txt',sep='\t')
SHindex = TRD_Index[TRD_Index.Indexcd == 1]
print(SHindex.head(3))

SZindex = TRD_Index[TRD_Index.Indexcd == 399106]

plt.scatter(SHindex.Retindex,SZindex.Retindex)
plt.title('上证综指与深证成指收益率')
plt.xlabel('上证综指收益率')
plt.ylabel('深证成指收益率')
plt.show()

# 计算上证综指与深证成指收益率的相关系数
SZindex.index = SHindex.index
prob = SZindex.Retindex.corr(SHindex.Retindex)
print(prob)