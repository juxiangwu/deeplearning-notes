#coding:utf-8
'''
自动求导
'''

from mxnet import ndarray as nd
from mxnet import autograd as ag

# 函数f = 2 * x^2
x = nd.array([[1,2],[3,4]])

# 向系统申请对x进行求导
x.attach_grad()

# 显式记录要求求导的函数
with ag.record():
    y = x * 2
    z = y * x

# 对函数进行求导
z.backward()
print('x.grad:',x.grad)

'''
对控制流进行求导
'''
def f(a):
    b = a * 2
    while nd.norm(b).asscalar() < 1000:
        b = b * 2
    if nd.sum(b).asscalar() > 0:
        c = b
    else:
        c = 100 * b
    return c

a = nd.random_normal(shape=3)
a.attach_grad()
with ag.record():
    c = f(a)

c.backward()

print('c.grad = ',a.grad)