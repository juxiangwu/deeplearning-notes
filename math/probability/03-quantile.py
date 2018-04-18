#coding:utf-8
'''
分位数
'''

from collections import Counter

def quantile(v,p):
    idx = int(len(v) * p)
    return sorted(v)[idx]

v = [1,3,-1,5,4,2,-10]
print('quantile:',quantile(v,0.1))