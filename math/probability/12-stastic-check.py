#coding:utf-8
'''
统计假设检验
'''
import random
from collections import Counter
import matplotlib.pyplot as plt
import math

from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

# 正态分布的累积分布
def normal_cdf(x, mu=0,sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

# 求CDF的逆
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

# 伯努利随机数
def bernoulli_trial(p):
    return 1 if random.random() < p else 0

# 中心极限定理
def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

def normal_approximation_to_binomail(n,p):
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu,sigma

normal_probability_bellow = normal_cdf

def normal_probability_above(lo,mu=0,sigma=1):
    return 1 - normal_cdf(lo,mu,sigma)

def normal_probability_between(lo,hi,mu=0,sigma=1):
    return normal_cdf(hi,mu,sigma) - normal_cdf(lo,mu,sigma)

def normal_probability_outside(lo,hi,mu=0,sigma=1):
    return 1 - normal_probability_between(lo,hi,mu,sigma)

def normal_upper_bound(probability,mu=0,sigma = 1):
    return inverse_normal_cdf(probability,mu,sigma)

def normal_lower_bound(probability,mu=0,sigma = 1):
    return inverse_normal_cdf(1 - probability,mu,sigma)

def normal_two_sided_bounds(probability,mu=0,sigma=1):
    tail_probability = (1 - probability) / 2
    upper_bound = normal_lower_bound(tail_probability,mu,sigma)

    lower_bound = normal_upper_bound(tail_probability,mu,sigma)

    return lower_bound,upper_bound