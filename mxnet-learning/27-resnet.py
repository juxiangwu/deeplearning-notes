#coding:utf-8
'''
ResNet
'''
from mxnet.gluon import nn
from mxnet import nd
import sys
import os
sys.path.append(os.getcwd())
import utils
from mxnet import gluon
from mxnet import init

class Residual(nn.Block):
    def __init__(self,channels,same_shape=True,**kwargs):
        super(Residual,self).__init__(**kwargs)

        self.same_shape = same_shape
        strides = 1 if same_shape else 2
        
        self.conv1 = nn.Conv2D(channels,kernel_size=3,
                padding=1,strides=strides)
        self.bn1 = nn.BatchNorm()

        self.conv2 = nn.Conv2D(channels,kernel_size=3,
                    padding=1)
        self.bn2 = nn.BatchNorm()

        if not same_shape:
            self.conv3 = nn.Conv2D(channels,kernel_size=1,
                strides=strides)

    def forward(self,x):
        out = nd.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))

        if not self.same_shape:
            x = self.conv3(x)
        
        return nd.relu(out+x)

blk = Residual(3)
blk.initialize()

x = nd.random.uniform(shape=(4,3,6,6))
result = blk(x)
print(result.shape)

blk2 = Residual(8,same_shape=False)
blk2.initialize()
result = blk2(x)
print(result.shape)

class ResNet(nn.Block):
    def __init__(self,num_class,verbose = False,**kwargs):
        super(ResNet,self).__init__(**kwargs)
        self.verbose = verbose
        with self.name_scope():
            # block 1
            b1 = nn.Conv2D(64,kernel_size=7,strides=2)
            # block 2
            b2 = nn.Sequential()
            b2.add(
                nn.MaxPool2D(pool_size=3,strides=2),
                Residual(64),
                Residual(64)
            )

            # block 3
            b3 = nn.Sequential()
            b3.add(
                Residual(128,same_shape=False),
                Residual(128)
            )

            # block 4
            b4 = nn.Sequential()
            b4.add(
                Residual(256,same_shape=False),
                Residual(256)
            )

            # block 5
            b5 = nn.Sequential()
            b5.add(
                Residual(512,same_shape=False),
                Residual(512)
            )

            # block 6
            b6 = nn.Sequential()
            b6.add(
                nn.AvgPool2D(pool_size=3),
                nn.Dense(num_class))
            
            self.net = nn.Sequential()
            self.net.add(b1,b2,b3,b4,b5,b6)

    def forward(self,x):
        out = x
        for i ,b in enumerate(self.net):
            out = b(out)
            if self.verbose:
                print('Block %d output: %s'%(i+1, out.shape))
        return out

net = ResNet(10, verbose=True)
net.initialize()
x = nd.random.uniform(shape=(4, 3, 96, 96))
y = net(x)
print(y)

train_data, test_data = utils.load_data_fashion_mnist(batch_size=64, resize=96)
ctx = utils.try_gpu()
net = ResNet(10)
net.initialize(ctx=ctx, init=init.Xavier())
loss = gluon.loss.SoftmaxCrossEntropyLoss()
trainer = gluon.Trainer(net.collect_params(),'sgd', {'learning_rate': 0.05})
utils.train(train_data, test_data, net, loss,trainer, ctx, num_epochs=5)