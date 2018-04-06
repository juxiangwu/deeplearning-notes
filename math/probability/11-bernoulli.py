#coding:utf-8
'''
二项分布与正态近似
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

# 伯努利随机数
def bernoulli_trial(p):
    return 1 if random.random() < p else 0

# 中心极限定理
def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

def make_hist(p,n,num_points):
    data = [binomial(n,p) for _ in range(num_points)]

    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
            [v / num_points for v in histogram.values()],
            0.8,color='0.75')
    
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))

    # 绘制正态近似
    xs = range(min(data),max(data) + 1)
    ys = [normal_cdf(i + 0.5,mu,sigma) - normal_cdf(i - 0.5,mu,sigma) for i in xs]

    plt.plot(xs,ys)
    plt.title(u'二项分布与正态近似')
    plt.show()

make_hist(0.55,100,10000)