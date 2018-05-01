#coding:utf-8
'''
两个隐藏层的多层感知机
'''
from mxnet import gluon
from mxnet import ndarray
from mxnet import autograd
import numpy as np
import matplotlib.pyplot as plt
from mxnet import nd

def transform(data,label):
    return data.astype('float32') / 255,label.astype('float32')

def dropout(X,drop_probability):
    keep_probability = 1 - drop_probability
    assert 0 <= keep_probability <= 1
    if keep_probability == 0:
        return X.zeros_like()
    # 随机选择一部分该层的输出
    mask = nd.random.uniform(0,1.0,X.shape,ctx=X.context) < keep_probability
    scale = 1 / keep_probability
    return mask * X * scale

def get_text_labels(label):
    text_labels = [
        't-shirt','trouser','pullover','dress','coat',
        'sandal','shirt','sneaker','bag','ankle boot'
    ]

    return [text_labels[int(i)] for i in label]

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

# 读取数据
mnist_train = gluon.data.vision.FashionMNIST(train=True,transform=transform)
mnist_test = gluon.data.vision.FashionMNIST(train=False,transform=transform)
batch_size = 256
train_data = gluon.data.DataLoader(mnist_train,batch_size,shuffle=True)
test_data = gluon.data.DataLoader(mnist_test,batch_size,shuffle=False)

num_inputs = 28*28
num_outputs = 10

num_hidden1 = 256
num_hidden2 = 256

weight_scale = 0.01

W1 = nd.random_normal(shape=(num_inputs, num_hidden1), scale=weight_scale)
b1 = nd.zeros(num_hidden1)
W2 = nd.random_normal(shape=(num_hidden1, num_hidden2), scale=weight_scale)
b2 = nd.zeros(num_hidden2)
W3 = nd.random_normal(shape=(num_hidden2, num_outputs), scale=weight_scale)
b3 = nd.zeros(num_outputs)
params = [W1, b1, W2, b2, W3, b3]

for param in params:
    param.attach_grad()

# 定义包含dropout层的模型

drop_prob1 = 0.2
drop_prob2 = 0.5

def net(X):
    X = X.reshape((-1,num_inputs))

    # 第一层全连接
    h1 = nd.relu(nd.dot(X,W1) + b1)

    # 添加Dropout层
    h1 = dropout(h1,drop_prob1)
    # 第二层全连接
    h2 = nd.relu(nd.dot(h1,W2) + b2)
    # 添加Dropout层
    h2 = dropout(h2,drop_prob2)
    return nd.dot(h2,W3) + b3


# 定义损失函数
softmax_cross_entropy = gluon.loss.SoftmaxCrossEntropyLoss()

# 定义学习速率
learning_rate = 0.5

# 定义训练迭代次数
epochs = 5
for epoch in range(epochs):
    train_loss = 0.0
    train_acc = 0.0

    for data,label in train_data:
        with autograd.record():
            output = net(data)
            loss = softmax_cross_entropy(output,label)
        
        loss.backward()
        SGD(params,learning_rate / batch_size)

         # 计算训练精度
        train_loss += nd.mean(loss).asscalar()
        train_acc += accuracy(output,label)

    test_acc = evaluate_accuracy(test_data,net)
    print('Epoch: %d, Loss %f, Train_Acc:%f, Test_Acc:%f .' %(epoch,train_loss/len(train_data),
            train_acc / len(train_data),test_acc))

# 预测
data, label = mnist_test[0:9]
# show_images(data)
print('true labels')
print(get_text_labels(label))
predicted_labels = net(data).argmax(axis=1)
print('predicted labels')
print(get_text_labels(predicted_labels.asnumpy()))








