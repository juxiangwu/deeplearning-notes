#coding:utf-8

'''
向量操作
'''
from functools import reduce

def vector_add(v,w):
    return[v_i + w_i for v_i,w_i in zip(v,w)]

def vector_subtract(v,w):
    return[v_i - w_i for v_i,w_i in zip(v,w)]

def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result,vector)
    return result

def vector_sum2(vectors):
    return reduce(vector_add,vectors)

def scalar_multiply(c, v):
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n,vector_sum(vectors))

def dot(v,w):
    return sum(v_i * w_i for v_i,w_i in zip(v,w))

def sum_of_squares(v):
    return dot(v,v)

# 计算向量大小
import math
def magnitude(v):
    return math.sqrt(sum_of_squares(v))

# 计算两个向量的距离
def squared_distance(v,w):
    return sum_of_squares(vector_subtract(v,w))

def distance(v,w):
    return math.sqrt(squared_distance(v,w))

v = [1,2,3,4,5,6,7,8,9]
w = [10,11,12,13,14,15,16,17,18]

print('vector add:',vector_add(v,w))
print('vector subtract:',vector_subtract(v,w))
print('vector sum:',vector_sum([v,w]))
print('vector sum2:',vector_sum2([v,w]))
print('vector mean:',vector_mean([v,w]))
print('vector dot:',dot(v,w))
print('vector sum of square:',sum_of_squares(v))
print('magnitude:',magnitude(v))
print('squared distance:',squared_distance(v,w))
print('distance:',distance(v,w))