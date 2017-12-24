# -*- coding: utf-8 -*-
import numpy as np

#全零矩阵
mzero = np.zeros([3,5])
print(mzero)

#全1矩阵
mones = np.zeros([3,3])
print(mones)

#生成随机矩阵
mrand = np.random.rand(3,4)
print(mrand)

#单位矩阵
meye = np.eye(3)
print(meye)

#矩阵相加减
mones = np.ones([3,3])
meye = np.eye(3)
res = mones + meye
print(res)
res = mones - meye
print(res)

#矩阵相乘
mmat = np.mat([[1,2,3],[4,5,6],[7,8,9]])
a = 10
res = a * mmat
print(res)

#矩阵所有元素求和
res = np.sum(mmat)
print('matrix sum:',res)

#计算矩阵元素的积
mmat2 = 1.5 * np.ones([3,3])
res = np.multiply(mmat,mmat2)
print('matrix multiply:\n',res)

#计算矩阵各元素的n次幂
res = np.power(mmat,2)
print('exp of matrix:\n',res)

#矩阵乘矩阵
mmat2 = np.mat([[1],[2],[3]])
res = mmat * mmat2
print('matrix multiply matrix:\n',res)

#矩阵的转置
T = mmat.T
print('matrix transform:\n',T)