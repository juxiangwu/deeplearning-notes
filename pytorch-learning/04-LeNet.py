#coding:utf-8
'''
LeNet神经网络
参考：http://www.cnblogs.com/hellcat/p/6858125.html
'''
import torch as T
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.autograd import Variable
import numpy as np

class LeNet(nn.Module):
    def __init__(self):
        super(LeNet,self).__init__()

        # 输入1通道，输出6通道，卷积核5*5
        self.conv1 = nn.Conv2d(1,6,5)

        #定义卷积层：输入6张特征图，输出16张特征图，卷积5*5
        self.conv2 = nn.Conv2d(6,16,5)

        # 定义全连接层：线性连接(y = Wx + b)，16*5*5个节点连接到120个节点上
        self.fc1 = nn.Linear(16*5*5,120)

        # 定义全连接层：线性连接(y = Wx + b),120个节点连接到84个节点上
        self.fc2 = nn.Linear(120,84)
        
        # 定义全连接层：线性连接(y = Wx + b)
        self.fc3 = nn.Linear(84,10)

    # 定义向前传播函数，并自动生成向后传播函数
    def forward(self,x):
        # 输入x->conv1->relu->2x2窗口的最大池化->更新到x
        x = F.max_pool2d(F.relu(self.conv1(x)),(2,2))

        # 输入x->conv2->relu->2x2窗口最大池化->更新到x
        x = F.max_pool2d(F.relu(self.conv2(x)),2)

        # view函数将张量x变成一维向量形式，总特征数不变，为全连接作准备
        x = x.view(x.size()[0],-1)

        # 输入x->fc1->relu,更新到x
        x = F.relu(self.fc1(x))

        # 输入x->fc2->relu,更新到x
        x = F.relu(self.fc2(x))

        # 输入x->fc3,更新到x
        x = self.fc3(x)

        return x

if __name__ == '__main__':
    net = LeNet()

    print(net)

    params = list(net.parameters())
    print(len(params))

    for name,parameters in net.named_parameters():
        print(name,":",parameters.size())

    input_data = Variable(T.randn(1,1,32,32))
    out = net(input_data)
    print(out.size())

    # 定义Loss函数
    target = Variable(T.from_numpy(np.arange(0,10,dtype=np.float32).reshape((1,10))))
    loss_fn = nn.MSELoss()
    loss = loss_fn(out,target)
    print(loss)

    net.zero_grad()
    print('before backward:',net.conv1.bias.grad)
    loss.backward()
    print('after backward:',net.conv1.bias.grad)

    # 定义优化器
    optimizer = optim.SGD(net.parameters(),lr=0.01)
    optimizer.zero_grad()
    output = net(input_data)
    loss = loss_fn(output,target)

    loss.backward()
    print('before backward:',net.conv1.bias.data)
    optimizer.step()
    print('after backward:',net.conv1.bias.data)