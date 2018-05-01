#coding:utf-8

from mxnet import ndarray as nd
import numpy as np

z = nd.zeros((3,4))
print('zeros:z = ',z)
o = nd.ones((3,4))
print('o = ',o)
# 从数组直接创建
n = nd.array([[1,2],[3,4]])
print('n = ',n)

# 创建服从均值为0，标准差为1的正态分布随机数组
y = nd.random_normal(0,1,shape=(3,4))
print('random_normal:y = ',y)

# 相加
a = z + o
print('z + o = \n',a)
# 相乘
b = z * y
print('z * y =',b)

# 指数运算
e = nd.exp(y)
print('exp(y):e = ',e)

res = nd.dot(o,y.T)
print('dot = ',res)

# 转换到 numpy数组
print('asnumpy:',res.asnumpy())

# 
x = nd.zeros_like(y)
nd.elemwise_add(y,y,out=x)
print('x = ',x)

x = nd.arange(0,9).reshape((3,3))
print('x = ',x)
print('x[1,2] = ',x[1,2])
print('x[1:2,1:3] = ',x[1:2,1:3])
x[1,2] = 9
print('x = ',x)
x[1:3,1:3] = 9
print('x = ',x)