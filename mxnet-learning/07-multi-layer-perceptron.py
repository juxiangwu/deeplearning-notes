#coding:utf-8
'''
多层感知机
'''
from mxnet import gluon
from mxnet import ndarray
from mxnet import autograd
import numpy as np
import matplotlib.pyplot as plt
from mxnet import nd

def transform(data,label):
    return data.astype('float32') / 255,label.astype('float32')

# 读取数据
mnist_train = gluon.data.vision.FashionMNIST(train=True,transform=transform)
mnist_test = gluon.data.vision.FashionMNIST(train=False,transform=transform)
batch_size = 256
train_data = gluon.data.DataLoader(mnist_train,batch_size,shuffle=True)
test_data = gluon.data.DataLoader(mnist_test,batch_size,shuffle=False)

num_inputs = 28*28
num_outputs = 10

# 定义感知机的隐含层节点
num_hidden = 256
weight_scale = 0.01

# 定义网络参数
W1 = nd.random_normal(shape=(num_inputs,num_hidden))
b1 = nd.zeros(num_hidden)

W2 = nd.random_normal(shape=(num_hidden,num_outputs))
b2 = nd.zeros(num_outputs)

params = [W1,b1,W2,b2]

# 参数求导申请
for param in params:
    param.attach_grad()

# 激活函数
def relu(X):
    return nd.maximum(X,0)

# 定义模型：将层全链接和激活函数串起来
def net(X):
    X = X.reshape((-1,num_inputs))
    h1 = relu(nd.dot(X,W1) + b1)
    output = nd.dot(h1,W2) + b2
    return output

# 定义交叉熵损失函数
softmax_cross_entropy = gluon.loss.SoftmaxCrossEntropyLoss()

# 优化器
def SGD(params,lr):
    for param in params:
        param[:] = param - lr * param.grad

# 定义精度计算
def accuracy(output,label):
    return nd.mean(output.argmax(axis=1) == label).asscalar()

# 估计模型精度
def evaluate_accuracy(data_iterator,net):
    acc = 0
    for data,label in data_iterator:
        output = net(data)
        acc += accuracy(output,label)
        return acc / len(data_iterator)

# 训练
learning_rate = 0.5

epochs = 5
for epoch in range(epochs):
    train_loss = 0.0
    train_acc = 0.0

    for data,label in train_data:
        with autograd.record():
            output =  net(data)
            loss = softmax_cross_entropy(output,label)

        loss.backward()
        SGD(params,learning_rate/batch_size)

        # 计算训练精度
        train_loss += nd.mean(loss).asscalar()
        train_acc += accuracy(output,label)

    test_acc = evaluate_accuracy(test_data,net)
    print('Epoch: %d, Loss %f, Train_Acc:%f, Test_Acc:%f .' %(epoch,train_loss/len(train_data),
            train_acc / len(train_data),test_acc))

def get_text_labels(label):
    text_labels = [
        't-shirt','trouser','pullover','dress','coat',
        'sandal','shirt','sneaker','bag','ankle boot'
    ]

    return [text_labels[int(i)] for i in label]

# 预测
data, label = mnist_test[0:9]
# show_images(data)
print('true labels')
print(get_text_labels(label))
predicted_labels = net(data).argmax(axis=1)
print('predicted labels')
print(get_text_labels(predicted_labels.asnumpy()))