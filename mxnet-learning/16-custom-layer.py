#coding:utf-8
'''
自定义层
'''
from mxnet import ndarray as nd
from mxnet import init
from mxnet import gluon
from mxnet.gluon import nn

class CenteredLayer(nn.Block):
    def __init__(self,**kwargs):
        super(CenteredLayer,self).__init__(**kwargs)

    def forward(self,x):
        return x - x.mean()

layer = CenteredLayer()
print(layer(nd.array([1,2,3,4,5])))

net = nn.Sequential()