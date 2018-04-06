#coding:utf-8
'''
使用二分查找法对正态分布的累积分布求逆
'''

import math

def normal_cdf(x, mu=0,sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p,mu=0,sigma=1,tolerance=0.00001):
    '''
    调整非标准型成服从标准型
    '''

    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    low_z, low_p = -10.0, 0 # normal_cdf(-10)是（非常接近）0
    hi_z, hi_p = 10.0, 1 # normal_cdf(10)是（非常接近）

    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)

        if mid_p < p:
            # 中点值太小，继续搜索比它大的值
            low_z,low_p = mid_z,mid_p
        elif mid_p > p:
            # 中点值太大，继续搜索比它小的值
            hi_z,hi_p = mid_z,mid_p
        else:
            break
    return mid_z
