#coding:utf-8
'''
读取和存储
'''

from mxnet import nd
from mxnet.gluon import nn
import mxnet as mx

x = nd.ones(3)
y = nd.zeros(4)

filename = 'datas/test1.params'
nd.save(filename,[x,y])

a,b = nd.load(filename)

print(a,b)

# 读写Gluon模型参数
def get_net():
    net = nn.Sequential()
    with net.name_scope():
        net.add(nn.Dense(10,activation='relu'))
        net.add(nn.Dense(2))

    return net

net =get_net()
net.initialize()
x = nd.random.uniform(shape=(2,10))
print(net(x))

filename = 'datas/mlp.params'
net.save_params(filename)

net2 = get_net()
net2.load_params(filename,mx.cpu())
print(net2(x))