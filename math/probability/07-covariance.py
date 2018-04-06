#coding:utf-8
'''
协方差
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

def standard_deviation(v):
    return math.sqrt(variance(v))

def covariance(v,w):
    n = len(v)
    return dot(de_mean(v),de_mean(w)) / (n - 1)

v = [1,2,3,4,6,8,0,10]
w = [2,30,4,8,10,20,1,10]

print('covirance:',covariance(v,w))