#coding:utf-8
'''
多类别分类
'''

from mxnet import gluon
from mxnet import ndarray
from mxnet import autograd
import numpy as np
import matplotlib.pyplot as plt
from mxnet import nd

def transform(data,label):
    return data.astype('float32') / 255,label.astype('float32')

mnist_train = gluon.data.vision.FashionMNIST(train=True,transform=transform)
mnist_test = gluon.data.vision.FashionMNIST(train=False,transform=transform)

# 显示样本的形状和标号
data,label = mnist_train[0]
print('shape:',data.shape,',label:',label)

def show_images(images):
    n = images.shape[0]
    _,figs = plt.subplots(1,n,figsize=(15,15))
    for i in range(n):
        figs[i].imshow(images[i].reshape((28,28)).asnumpy())
        figs[i].axes.get_xaxis().set_visible(False)
        figs[i].axes.get_yaxis().set_visible(False)

    plt.show()

def get_text_labels(label):
    text_labels = [
        't-shirt','trouser','pullover','dress','coat',
        'sandal','shirt','sneaker','bag','ankle boot'
    ]

    return [text_labels[int(i)] for i in label]
# 显示数据
# data,label = mnist_train[0:9]
# show_images(data)
# print(get_text_labels(label))

# 读取数据
batch_size = 64
train_data = gluon.data.DataLoader(mnist_train,batch_size,shuffle=True)
test_data = gluon.data.DataLoader(mnist_test,batch_size,shuffle=False)

# 初始化模型参数
num_inputs = 784
num_outputs = 10

W = nd.random_normal(shape=(num_inputs,num_outputs))
b = nd.random_normal(shape=num_outputs)
params = [W,b]
# 申请自动求导
for param in params:
    param.attach_grad()

# 定义模型
def softmax(X):
    exp = nd.exp(X)
    partition = exp.sum(axis = 1,keepdims = True)
    return exp / partition

# X = nd.random_normal(shape=(2,5))
# X_prob = softmax(X)
# print(X_prob)
# print(X_prob.sum(axis = 1))
# ots = nd.dot(X.reshape((-1,num_inputs)),W) + b
# print('X.reshape(-1,nums_input):',X.reshape((-1,num_inputs)).shape)
# print('ots.shape:',ots.shape)
# print('exp:',np.exp(ots.asnumpy()))
def net(X):
    return softmax(nd.dot(X.reshape((-1,num_inputs)),W) + b)

# 定义损失函数,交叉熵损失函数
def cross_entropy(yhat,y):
    return -nd.pick(nd.log(yhat),y)

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

# 优化器
def SGD(params,lr):
    for param in params:
        param[:] = param - lr * param.grad

# 训练

learning_rate = 0.1
epochs = 5
for epoch in range(epochs):
    train_loss = 0.0
    train_acc = 0.0

    for data,label in train_data:
        with autograd.record():
            output = net(data)
            loss = cross_entropy(output,label)
        
        loss.backward()

        SGD(params,learning_rate / batch_size)

        train_loss += nd.mean(loss).asscalar()
        train_acc += accuracy(output,label)

    test_acc = evaluate_accuracy(test_data,net)
    print('Epoch: %d, Loss %f, Train_Acc:%f, Test_Acc:%f .' %(epoch,train_loss/len(train_data),
            train_acc / len(train_data),test_acc))

# 预测
data, label = mnist_test[0:9]
show_images(data)
print('true labels')
print(get_text_labels(label))
predicted_labels = net(data).argmax(axis=1)
print('predicted labels')
print(get_text_labels(predicted_labels.asnumpy()))