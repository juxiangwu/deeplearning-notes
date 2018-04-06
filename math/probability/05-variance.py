#coding:utf-8
'''
方差
'''

def mean(v):
    if not v or len(v) == 0:
        print('invalid vector')
        return None
    return sum(v) / len(v)

def de_mean(v):
    x_bar = mean(v)
    res =  [x_i - x_bar for x_i in v]
    return res

def dot(v,w):
   return sum(v_i * w_i for v_i,w_i in zip(v,w))

def sum_of_squares(v):
    return dot(v,v)

def variance(v):
    n = len(v)
    deviations = de_mean(v)
    return sum_of_squares(deviations) / (n - 1)

v1 = [1,1,1,1,1,1,1,1,1,1]
v2 = [1,2,3,4,5,6,7,8,9,10]

print('variance:',variance(v1))
