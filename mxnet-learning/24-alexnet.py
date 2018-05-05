#coding:utf-8
'''
AlexNet实现
'''
from mxnet import ndarray as nd
from mxnet import gluon
from mxnet.gluon import nn
from mxnet import init
from mxnet import autograd
import sys
import os
sys.path.append(os.getcwd())
# from utils import accuracy,evaluate_accuracy,load_data_fashion_mnist
import utils

# 定义模型
net = nn.Sequential()
with net.name_scope():
    net.add(
    # 第一阶段
    nn.Conv2D(channels = 96,kernel_size=11,strides=4,activation='relu'),
    nn.MaxPool2D(pool_size=3,strides=2),

    # 第二阶段
    nn.Conv2D(channels=256,kernel_size=5,padding=2,activation='relu'),
    nn.MaxPool2D(pool_size=3,strides=2),

    # 第三阶段
    nn.Conv2D(channels=384,kernel_size=3,padding=1,activation='relu'),
    nn.Conv2D(channels=384,kernel_size=3,padding=1,activation='relu'),
    nn.Conv2D(channels=256,kernel_size=3,padding=1,activation='relu'),
    nn.MaxPool2D(pool_size=3,strides=2),

    # 第四阶段
    nn.Flatten(),
    nn.Dense(2094,activation='relu'),
    nn.Dropout(0.5),

    # 第五阶段
    nn.Dense(4096,activation='relu'),
    nn.Dropout(0.5),

    # 第六阶段
    nn.Dense(10)
    )
batch_size = 64
train_data,test_data = utils.load_data_fashion_mnist(batch_size=64,resize=244)

# 训练
learning_rate = 0.5
net.initialize(init=init.Xavier())
softmax_cross_entropy = gluon.loss.SoftmaxCrossEntropyLoss()
trainer = gluon.Trainer(net.collect_params(),'sgd',{'learning_rate':0.01})
epochs = 5
for epoch in range(epochs):
    train_loss = 0.0
    train_acc = 0.0

    for data,label in train_data:
        with autograd.record():
            output =  net(data)
            loss = softmax_cross_entropy(output,label)

        loss.backward()
        trainer.step(batch_size)
        # 计算训练精度
        train_loss += nd.mean(loss).asscalar()
        train_acc += utils.accuracy(output,label)
        print('train_loss = %f,train_acc = %f' % (train_loss,train_acc))

    test_acc = utils.evaluate_accuracy(test_data,net)
    print('Epoch: %d, Loss %f, Train_Acc:%f, Test_Acc:%f .' %(epoch,train_loss/len(train_data),
            train_acc / len(train_data),test_acc))

# def get_text_labels(label):
#     text_labels = [
#         't-shirt','trouser','pullover','dress','coat',
#         'sandal','shirt','sneaker','bag','ankle boot'
#     ]

#     return [text_labels[int(i)] for i in label]

# # 预测
# data, label = mnist_test[0:9]
# # show_images(data)
# print('true labels')
# print(get_text_labels(label))
# predicted_labels = net(data).argmax(axis=1)
# print('predicted labels')
# print(get_text_labels(predicted_labels.asnumpy()))