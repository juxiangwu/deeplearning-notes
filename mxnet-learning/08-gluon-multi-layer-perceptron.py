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

# 定义网络模型并初始化
net = gluon.nn.Sequential()
with net.name_scope():
    net.add(gluon.nn.Dense(256, activation='relu'))
    net.add(gluon.nn.Dense(10))

net.initialize()

# 定义损失函数
softmax_cross_entropy = gluon.loss.SoftmaxCrossEntropyLoss()

# 定义优化器
trainer = gluon.Trainer(net.collect_params(), 'sgd', {'learning_rate': 0.5})

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
epochs = 5
for epoch in range(epochs):
    train_loss = 0.0
    train_acc = 0.0
    for data,label in train_data:
        with autograd.record():
            output = net(data)
            loss = softmax_cross_entropy(output,label)
        loss.backward()
        trainer.step(batch_size)

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