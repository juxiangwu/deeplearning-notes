#coding:utf-8
import torch  
import torchvision  
import torchvision.transforms as transforms  
  
transform = transforms.Compose(  
    [transforms.ToTensor(),  
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))]  
)  
dataset_dir = 'D:/Develop/DeepLearning/datasets'
trainset = torchvision.datasets.CIFAR10(root=dataset_dir, train=True, download=True, transform=transform)  
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4, shuffle=True, num_workers=2)  # 2线程读取数据  
testset = torchvision.datasets.CIFAR10(root=dataset_dir, train=False, download=True, transform=transform)  
testloader = torch.utils.data.DataLoader(testset, batch_size=4, shuffle=False, num_workers=2)  
classes = ('plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')  
  
import matplotlib.pyplot as plt  
import numpy as np  
  
def imshow(img):  
    img = img / 2 + 0.5     # [-1, 1] -> [0, 1]  
    npimg = img.numpy()  
    plt.imshow(np.transpose(npimg, (1, 2, 0)))  
  
  
#get some random training images  
# dataiter = iter(trainloader)  
# images, labels = dataiter.next()  
#  
# imshow(torchvision.utils.make_grid(images))  
# print(''.join('%5s' % classes[labels[j]] for j in range(4)))  
# plt.show()  
  
  
from torch.autograd import Variable  
import torch.nn as nn  
import torch.nn.functional as F  
  
class Net(nn.Module):  
    def __init__(self):  
        super(Net, self).__init__()  
        self.conv1 = nn.Conv2d(3, 6, 5)  
        self.pool = nn.MaxPool2d(2, 2)  
        self.conv2 = nn.Conv2d(6, 16, 5)  
        self.fc1 = nn.Linear(16*5*5, 120)  
        self.fc2 = nn.Linear(120, 84)  
        self.fc3 = nn.Linear(84, 10)  
  
    def forward(self, x):  
        x = self.pool(F.relu(self.conv1(x)))  
        x = self.pool(F.relu(self.conv2(x)))  
        x = x.view(-1, 16*5*5)  
        x = F.relu(self.fc1(x))  
        x = F.relu(self.fc2(x))  
        x = self.fc3(x)  
        return x  
  
net = Net()  
  
import torch.optim as optim  
criterion = nn.CrossEntropyLoss()  
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)  
  
for epoch in range(2):  
    running_loss = 0.0  
    for i, data in enumerate(trainloader, 0):   # enumerate可以接收第二个参数，用于指定索引起始值  
        inputs, labels = data  
        inputs, labels = Variable(inputs), Variable(labels)  
  
        optimizer.zero_grad()  
  
        outputs = net(inputs)  
        loss = criterion(outputs, labels)  
        loss.backward()  
        optimizer.step()  
  
        running_loss += loss.data[0]  # 将torch.tensor变量loss.data变为realnumber(真实数据)loss.data[0]  
        if i % 2000 == 1999:  
            print('[%d, %5d] loss: %.3f' % (epoch + 1, i + 1, running_loss / 2000))  
            running_loss = 0.0  
  
print('Finished Training')  
  
dataiter = iter(testloader)  
images, labels = dataiter.next()  
# imshow(torchvision.utils.make_grid(images))  
  
print('GroundTruth: ', ' '.join('%5s' % classes[labels[j]] for j in range(4)))  
  
outputs = net(Variable(images))  
_, predicted = torch.max(outputs.data, 1)  
print('Predicted: ', ' '.join('%5s' % classes[predicted[j][0]] for j in range(4)))  # predicted是一个4*1的张量,predicted[j][0]以保证turple索引的是一个数  
# plt.show()  
  
correct = 0  
total = 0  
for data in testloader:  
    images, labels = data  
    outputs = net(Variable(images))  
    _, predicted = torch.max(outputs.data, 1)  
    total += labels.size(0)  
    correct += (predicted == labels).sum()  
print('Accuracy of the network on the 10000 test images: %d %% \n' % (100 * correct / total))  
  
class_correct = list(0. for i in range(10))  
class_total = list(0. for i in range(10))  
for data in testloader:  
    images, labels = data                # labels shape -> (4,)  
    outputs = net(Variable(images))      # predicted shape -> (4, 1)  
    _, predicted = torch.max(outputs.data, 1)  
    c = (predicted == labels)  # squeeze(), return a tensor with all the dimensions of input of size 1 removed  
    c = c.squeeze()            # translate shape from (4*1) to (4)  
    for i in range(4):  
        label = labels[i]  
        class_correct[label] += c[i]  
        class_total[label] += 1  
  
for i in range(10):  
    print('Accuracy of %5s : %2d %%' % (classes[i], 100 * class_correct[i] / class_total[i]))  