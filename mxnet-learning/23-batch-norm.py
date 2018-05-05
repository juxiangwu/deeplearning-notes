#coding:utf-8
'''
批量归一化
'''

import mxnet as mx
from mxnet import gluon
from mxnet.gluon import nn
from mxnet import ndarray as nd

def pure_batch_norm(X,gamma,beta,eps = 1e-5):
    assert len(X.shape) in (2,4)
    # 全连接:batch_size * feature
    if len(X.shape) == 2:
        mean = X.mean(axis = 0)
        variance = ((X - mean) ** 2).mean(axis = 0)

    # 2D卷积:batch_size * channel * height * width
    else:
        mean = X.mean(axis = (0,2,3),keepdims = True)
        variance = ((X - mean) ** 2).mean(axis = (0,2,3),keepdims = True)
    # 均一化
    X_hat = (X - mean) / nd.sqrt(variance + eps)

    # 拉升和偏移
    return gamma.reshape(mean.shape) * X_hat + beta.reshape(mean.shape)

def batch_norm(X,gamma,beta,is_training,
            moving_mean,moving_variance,eps=1e-5,
            moving_momentum=0.9):
    assert len(X.shape) in (2,4)

    if len(X.shape) == 2:
        mean = X.mean(axis = 0)
        variance = ((X - mean) ** 2).mean(axis = 0)

    else:
        mean = X.mean(axis = (0,2,3),keepdims = True)
        variance = ((X - mean)**2).mean(axis = (0,2,3),keepdims = True)

        # 变形使得可以正确广播
        moving_mean = moving_mean.reshape(mean.reshape)
        moving_variance = moving_variance.reshape(mean.shape)

    if is_training:
        X_hat = (X - mean) / nd.sqrt(variance + eps)

        # 更新全局的均值方差
        moving_mean[:] = moving_momentum * moving_mean + (1.0 - moving_momentum) * variance

    else:
        X_hat = (X - moving_mean) / nd.sqrt(moving_variance + eps)
    
    # 拉升和偏移
    return gamma.reshape(mean.shape) * X_hat + beta.reshape(mean.shape)


A = nd.arange(6).reshape((3,2))
B = nd.arange(18).reshape((1,2,3,3))

A_batch = pure_batch_norm(A,gamma = nd.array([1,1]),beta = nd.array([0,0]))
print(A_batch)
B_batch = pure_batch_norm(B,gamma = nd.array([1,1]),beta = nd.array([0,0]))
print(B_batch)

