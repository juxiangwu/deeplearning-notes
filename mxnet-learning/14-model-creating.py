#coding:utf-8
'''
创建模型
'''
from mxnet import gluon
from mxnet import ndarray as nd
# 定义简单多层感知机模型
class MLP(gluon.nn.Block):
    def __init__(self,**kwargs):
        super(MLP,self).__init__(**kwargs)
        with self.name_scope():
            self.hidden = gluon.nn.Dense(256,activation='relu')
            self.output = gluon.nn.Dense(10)

    def forward(self,x):
        return self.output(self.hidden(x))

net = MLP()
net.initialize()
print('hidden layer name:',net.hidden.name)
print('output layer name:',net.output.name)
net = MLP(prefix='my_mlp_')
print('hidden layer name:',net.hidden.name)
print('output layer name:',net.output.name)

class MLP_NO_NAME_SCOPE(gluon.nn.Block):
    def __init__(self,**kwargs):
        super(MLP_NO_NAME_SCOPE,self).__init__(**kwargs)

        self.hidden = gluon.nn.Dense(256,activation='relu')
        self.output = gluon.nn.Dense(10)

    
    def forward(self,x):
        return self.output(self.hidden(x))

net = MLP_NO_NAME_SCOPE(prefix='my_mlp_')
net.initialize()
print('hidden layer name:',net.hidden.name)
print('output layer name:',net.output.name)

class FancyMLP(gluon.nn.Block):
    def __init__(self,**kwargs):
        super(FancyMLP,self).__init__(**kwargs)
        self.rand_weight = nd.random_uniform(shape=(10,20))
        with self.name_scope():
            self.dense = gluon.nn.Dense(10,activation='relu')

        
    def forward(self,x):
        x = self.dense(x)
        x = nd.relu(nd.dot(x,self.rand_weight) + 1)
        x = self.dense(x)
        return x

# 嵌套
class NestMLP(gluon.nn.Block):
    def __init__(self,**kwargs):
        super(NestMLP,self).__init__(**kwargs)
        self.net = gluon.nn.Sequential()
        with self.name_scope():
            self.net.add(gluon.nn.Dense(64,activation='relu'))
            self.net.add(gluon.nn.Dense(32,activation='relu'))
            self.dense = gluon.nn.Dense(16,activation='relu')

    def forward(self,x):
        return self.dense(self.net(x))

net = gluon.nn.Sequential()
net.add(NestMLP())
net.add(gluon.nn.Dense(10))
net.initialize()
print(net)