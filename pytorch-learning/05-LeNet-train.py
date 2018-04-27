#coding:utf-8
'''
LeNet神经网络训练
'''

import torch as T
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.autograd import Variable
import numpy as np
from torchvision import transforms, datasets as ds
from torch.utils.data import DataLoader

class LeNet(nn.Module):
    def __init__(self):
        super(LeNet,self).__init__()

        # 输入1通道，输出6通道，卷积核5*5
        self.conv1 = nn.Conv2d(3,6,5)

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
    data_dir = 'D:/Develop/DeepLearning/datasets/'
    transform = transforms.Compose([transforms.ToTensor()])
    train_set = ds.CIFAR100(root=data_dir, train=True, transform=transform, target_transform=None, 
                            download=True)
    
    trainloader = DataLoader(dataset=train_set,
                         batch_size=1,
                         shuffle=False,
                         num_workers=2)

    loss_fun = nn.CrossEntropyLoss()
    optimizer = optim.SGD(net.parameters(),lr=0.001,momentum=0.9)

    for step,data in enumerate(trainloader,0):
        inputs,labels = data
        inputs, labels = T.autograd.Variable(inputs), T.autograd.Variable(labels)

        # 梯度清零
        optimizer.zero_grad()

        # 向前传播
        outputs = net(inputs)
        print('output.size = ',outputs.size())
        print('labels.size = ',labels.size())
        # 反射传播
        loss = loss_fun(outputs,labels)
        loss.backward()

        # 更新数据
        optimizer.step()

        running_loss += loss.data[0]
        if step % 100 == 99:
            print('[{0:d},{1:5d}] loss:{2:3f}'.format(epoch+1,step+1,running_loss / 100))
            running_loss = 0.0

    print('finished training')

