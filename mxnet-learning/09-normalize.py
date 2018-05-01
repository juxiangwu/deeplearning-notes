#coding:utf-8
'''
正则化
高维线性回归
'''

from mxnet import gluon
from mxnet import ndarray
from mxnet import autograd
import numpy as np
import matplotlib.pyplot as plt
from mxnet import nd
import random

num_train = 20
num_test = 100
num_inputs = 200
batch_size = 1
#模型真实参数
true_w = nd.ones((num_inputs,1))
true_b = 0.05

#生成测试和训练数据
X = nd.random.normal(shape=(num_train+num_test,num_inputs))
y = nd.dot(X,true_w) + true_b
y += 0.01 * nd.random.normal(shape=y.shape)

X_train,X_test = X[:num_train,:],X[num_train:,:]
y_train,y_test = y[:num_train],y[num_train:]


def data_iter(num_exaples):
    batch_size = 1
    idx = list(range(num_exaples))
    random.shuffle(idx)
    for i in range(0,num_exaples,batch_size):
        j = nd.array(idx[i:min(i+batch_size,num_exaples)])
        yield X.take(j),y.take(j)

# 初始化模型参数
def init_params():
    w = nd.random_normal(scale=1,shape=(num_inputs,1))
    b = nd.zeros(shape=(1,))
    params = [w,b]
    for param in params:
        param.attach_grad()
    return params


# L2范数正则化
def L2_penalty(w,b):
    return ((w * 2).sum() + b ** 2) / 2

# 定义模型
def net(X,w,b):
    return nd.dot(X,w) + b

# 定义损失函数
def square_loss(yhat,y):
    return (yhat - y.reshape(yhat.shape)) ** 2 / 2

# 定义优化器
def sgd(params,learning_rate):
    for param in params:
        param[:] = param - learning_rate * param.grad / batch_size

# 定义测试函数
def test(net,params,X,y):
    return square_loss(net(X,*params),y).mean().asscalar()

# 定义训练函数
def train(lambd):
    epochs = 10
    learning_rate = 0.005
    w,b = params = init_params()
   
    train_loss = []
    test_loss = []

    for e in range(epochs):
        for data,label in data_iter(num_train):
            with autograd.record():
                output = net(data,*params)
                loss = square_loss(output,label) + lambd * L2_penalty(*params)
            loss.backward()
            sgd(params,learning_rate)

        train_loss.append(test(net,params,X_train,y_train))
        test_loss.append(test(net,params,X_test,y_test))

    plt.plot(train_loss)
    plt.plot(test_loss)
    plt.legend(['train','test'])
    plt.show()

# 未正则化
# train(0)

# 使用正则化
train(5)

