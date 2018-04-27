#coding:utf-8
'''
自动求导
'''

import torch
from torch.autograd import Variable

x = Variable(torch.ones(2,2),requires_grad=True)
y = x + 2

z = y * y * 3
out = z.mean()
out.backward()

print('x = ',x)
print('y = ',y)
print('z = ',z)
# 对out进行对x求导的结果
print('x.grad = ',x.grad)
# 输出结果应该为None
print('y.grad = ',y.grad)

x = torch.randn(3)
x = Variable(x,requires_grad=True)
y = x * 2

while y.data.norm() < 1000:
    y = y * 2

# 对y在某个梯度方向求导
gradients = torch.FloatTensor([0.1,1.0,10.0001])
y.backward(gradients)
print('x.grad = ',x.grad)
