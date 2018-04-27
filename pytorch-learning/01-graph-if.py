#coding:utf-8
'''
静态图
参考:http://www.cnblogs.com/hellcat/p/8436955.html
'''

import torch as T
from torch.autograd import Variable

def graph_if():
    x = Variable(T.randn(3,4))
    w1 = Variable(T.randn(4,5))
    w2 = Variable(T.randn(4,5))

    z = 10
    if z > 0:
        y = x.mm(w1)
    else:
        y = x.mm(w2)

    return y

if __name__ == '__main__':
    print(graph_if())