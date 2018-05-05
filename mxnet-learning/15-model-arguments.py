#coding:utf-8
'''
模型参数
'''
from mxnet import ndarray as nd
from mxnet import init
from mxnet import gluon
from mxnet.gluon import nn

# 定义简单多层感知机模型
class MLP(gluon.nn.Block):
    def __init__(self,**kwargs):
        super(MLP,self).__init__(**kwargs)
        with self.name_scope():
            self.hidden = gluon.nn.Dense(256,activation='relu')
            self.output = gluon.nn.Dense(10)

    def forward(self,x):
        return self.output(self.hidden(x))

# 访问模型参数
my_param = gluon.Parameter('good_param',shape=(2,3))
# 参数初始化
my_param.initialize()
print('data:',my_param.data())
print('grad:',my_param.grad())
print('name:',my_param.name)

# 初始化模型参数
x = nd.random.uniform(shape=(3, 5))
net = MLP()
net.initialize()
net(x)
params = net.collect_params()
params.initialize(init=init.Normal(sigma=0.02),force_reinit=True)
print('hidden weight: ', net.hidden.weight.data(), '\nhidden bias: ',
        net.hidden.bias.data(), '\noutput weight: ', net.output.weight.data(),
        '\noutput bias: ',net.output.bias.data())

# 自定义初始化
class MyInit(init.Initializer):
    def __init__(self):
        super(MyInit,self).__init__()
        self._verbose = True

    def _init_weight(self,_,arr):
        # 初始化权重
        nd.random.uniform(low=10,high=20,out=arr)

net = MLP()
net.initialize(MyInit())
net(x)
print(net.hidden.weight.data())

# 共享模型参数
net = nn.Sequential()
with net.name_scope():
    net.add(nn.Dense(4,activation='relu'))
    net.add(nn.Dense(4,activation='relu'))

    # 通过params 指定需要共享的模型参数
    net.add(nn.Dense(4,activation='relu',params=net[1].params))
    net.add(nn.Dense(2))

net.initialize()
net(x)
print(net[1].weight.data())
print(net[2].weight.data())