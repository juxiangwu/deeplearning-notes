#coding:utf-8
'''
正则化
'''
import mxnet as mx
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
#模型真实参数
true_w = nd.ones((num_inputs,1))
true_b = 0.05

#生成测试和训练数据
X = nd.random.normal(shape=(num_train+num_test,num_inputs))
y = nd.dot(X,true_w) + true_b
y += 0.01 * nd.random.normal(shape=y.shape)

X_train,X_test = X[:num_train,:],X[num_train:,:]
y_train,y_test = y[:num_train],y[num_train:]

batch_size = 1
dataset_train = gluon.data.ArrayDataset(X_train, y_train)
data_iter_train = gluon.data.DataLoader(dataset_train, batch_size,shuffle=True)

# 定义损失函数
square_loss = gluon.loss.L2Loss()

# 定义测试函数
def test(net,X,y):
    return square_loss(net(X),y).mean().asscalar()

# 定义训练函数
def train(weight_decay):
    epochs = 10
    learning_rate = 0.005
    net = gluon.nn.Sequential()
    with net.name_scope():
        net.add(gluon.nn.Dense(1))
    
    net.collect_params().initialize()
    trainer = gluon.Trainer(net.collect_params(),'sgd',
            {'learning_rate':learning_rate,'wd':weight_decay})

    train_loss = []
    test_loss = []

    for e in range(epochs):
        for data,label in data_iter_train:
            with autograd.record():
                output = net(data)
                loss = square_loss(output,label)
            loss.backward()
            trainer.step(batch_size)

        train_loss.append(test(net,X_train,y_train))
        test_loss.append(test(net,X_test,y_test))

    
    plt.plot(train_loss)
    plt.plot(test_loss)
    plt.legend(['train','test'])
    plt.show()

# 未使用正则化
# train(0)

# 使用正则化
train(5)