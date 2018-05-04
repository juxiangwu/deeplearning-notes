#coding:utf-8
'''
卷积计算
'''
import mxnet as mx
from mxnet.gluon import nn
from mxnet import ndarray as nd

# 卷积层
# 输入输出的数据格式是： batch * channel * height * width
# 权重格式：output_channels * in_channels * height * width

w = nd.arange(4).reshape((1,1,2,2))
b = nd.array([1])

data = nd.arange(9).reshape((1,1,3,3))

# 卷积运算
out = nd.Convolution(data,w,b,kernel=w.shape[2:],num_filter=w.shape[1])
print('input:',data)
print('weight:',w)
print('bias:',b)
print('output:',out)

# 窗口移动和边缘填充
out = nd.Convolution(data,w,b,kernel=w.shape[2:],
        num_filter=w.shape[1],stride=(2,2),pad=(1,1))

print('output:',out)

# 多通道数据卷积：每个通道会有相应的权重，然后对每个通道做卷积之后，在通道之间求和
data = nd.arange(18).reshape((1,2,3,3))
w = nd.arange(8).reshape((1,2,2,2))
out = nd.Convolution(data,w,b,kernel=w.shape[2:],num_filter=w.shape[0])
print('weight = ',w)
print('data = ',data)
print('output = ',out)

# Pooling
data = nd.arange(18).reshape((1,2,3,3))
max_pool = nd.Pooling(data=data, pool_type="max", kernel=(2,2))
avg_pool = nd.Pooling(data=data, pool_type="avg", kernel=(2,2))
print('data = ',data)
print('max pool = ',max_pool)
print('avg pool = ',avg_pool)

