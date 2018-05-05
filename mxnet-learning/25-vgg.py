#coding:utf-8
'''
VGG网络
'''
from mxnet.gluon import nn
from mxnet import ndarray as nd
import mxnet as mx
from mxnet import init
import os
import sys
sys.path.append(os.getcwd())
import utils

def vgg_block(num_convs,channels):
    out = nn.Sequential()
    for _ in range(num_convs):
        out.add(
            nn.Conv2D(channels=channels,kernel_size=3,padding=1,activation='relu')
        )

    out.add(nn.MaxPool2D(pool_size=2,strides=2))

    return out

# 将 vgg_block堆起来
def vgg_stack(arhitechure):
    out = nn.Sequential()
    for(num_convs,channels) in arhitechure:
        out.add(vgg_block(num_convs,channels))

    return out

blk = vgg_block(2,128)
blk.initialize()

x = nd.random.uniform(shape=(2,3,16,16))
y = blk(x)
print(y.shape)

# 定义一个最简单的VGG结构，8个卷积层，3个全连接层，称为VGG11
ctx = utils.try_gpu()
num_outputs = 10
architechure = ((1,64),(1,128),(2,256),(2,512),(2,512))
net = nn.Sequential()
with net.name_scope():
    net.add(
        vgg_stack(architechure),
        nn.Flatten(),
        nn.Dense(4096,activation='relu'),
        nn.Dropout(0.5),
        nn.Dense(4096,activation='relu'),
        nn.Dropout(0.5),
        nn.Dense(num_outputs)
    )

# 训练模型
train_data,test_data = utils.load_data_fashion_mnist(batch_size=64,
            resize=96)
ctx = utils.try_gpu()
net.initialize(ctx=ctx,init=init.Xavier())

loss = mx.gluon.loss.SoftmaxCrossEntropyLoss()
trainer = mx.gluon.Trainer(net.collect_params(),'sgd',{'learning_rate':0.05})

utils.train(train_data,test_data,net,loss,trainer,ctx,num_epochs=5)


