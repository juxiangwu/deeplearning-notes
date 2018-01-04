# -*- coding:utf-8 -*-
'''
独立样本t检验
'''

import numpy as np
import pandas as pd
from pylab import mpl 
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt
from scipy import stats

TRD_Index = pd.read_table('datas/qi/15/TRD_Index.txt',sep="\t")
SHindex = TRD_Index[TRD_Index.Indexcd == 1]
SHRet = SHindex.Retindex

ZHindex = TRD_Index[TRD_Index.Indexcd == 339106]
ZHRet = ZHindex.Retindex

res = stats.ttest_ind(SHRet,ZHRet)
print(res)