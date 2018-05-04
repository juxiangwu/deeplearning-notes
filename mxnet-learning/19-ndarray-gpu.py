#coding:utf-8
'''
NDArray在GPU上计算
'''

from mxnet import nd
from mxnet.gluon import nn
import mxnet as mx

a = nd.array([1,2,3],ctx=mx.gpu())
b = nd.zeros((3,2),ctx=mx.gpu())
x = nd.array([1,2,3])

y = x.copyto(mx.gpu())

z = x.as_in_context(mx.gpu())

print('a = ',a)
print('b = ',b)
print('x = ',x)
print('y = ',y)
print('z = ',z)

# Gluon的GPU计算

net = nn.Sequential()
net.add(nn.Dense(1))
net.initialize(ctx = mx.gpu())

data = nd.random.uniform(shape=(3,2),ctx=mx.gpu())
print(net(data))

# 模型的参数也储存在GPU上
print(net[0].weight.data())