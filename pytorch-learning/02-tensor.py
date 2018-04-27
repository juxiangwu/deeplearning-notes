#coding:utf-8
'''
张量
http://www.cnblogs.com/hellcat/p/6850256.html
'''
import torch
import numpy as np
# 初始化
x = torch.Tensor(5,3)
print('x = ',x)

# 通过随机数初始化
x = torch.randn(5,3)
print('x = ',x,',size = ',x.size())

# 加法操作
a = torch.ones(3,3)
b = torch.zeros(3,3)

print('a + b = ',a + b)
print('torch.add(a,b) = ',torch.add(a,b))
# 改变张量a的值
print('b.add_(a) = ',b.add_(a))
c = torch.Tensor(3,3)
torch.add(a,b,out=c)
print('torch.add(a,b,out=c) = ',c)

a = torch.ones(4,4)
# Tensor转换成numpy的array，两者内存共享,属于拷贝
b = a.numpy()
print('before:',b)
a.add_(1)
print('after:b=',b)
print('after:a=',a)

# numpy的array转换成Tensor,同样是内存共享
c = np.ones(5)
d = torch.from_numpy(c)
print('before:d=',d)
np.add(d,1,out=c)
print('c = ',c)
print('after:d=',d)

# 除了CharTensor之外，所有的Tensor都可以在CPU和CUDA设备之间相互转换
x = torch.ones(2,2)
y = torch.ones(2,2)

if torch.cuda.is_available():
    x = x.cuda()
    y = y.cuda()

print(x,y)
