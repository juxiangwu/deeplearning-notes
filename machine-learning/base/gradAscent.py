# -*- coding:utf-8 -*-
'''
#批梯度上升算法
'''

import numpy as np
import math
import matplotlib.pyplot as plt

def sigmoid(inX):  
    return 1.0/(1+np.exp(-inX)) 

def gradAscent(X,Y):  
    X=np.array(X)  
    m,n=np.shape(X)  
    Y=np.array(Y).reshape(m,1) #转化为列向量的形式  
    alpha = 0.01               #定义步长  
    iteration=400  
    thea = np.ones((n, 1)) #定义初始的点  
    for k in range(iteration):  
        H=sigmoid(X.dot(thea))  
        error=Y-H  
        thea=thea+alpha*X.T.dot(error)  
    return thea

