# -*- coding:utf-8 -*-

import numpy as np  
import matplotlib.pyplot as plt  
#导入数据  
def ReadFile(filename):  
    data=[]  
    label=[]  
    lines=open(filename,encoding='utf-8').readlines()  
    for i in range(len(lines)):  
        xy=lines[i].strip().split(',')  
        data.append([1,float(xy[0])])  
        label.append(float(xy[1]))  
    return data,label  
  
#定义代价函数  
def costfunction(X,Y,thea):  
    m=np.shape(Y)[0]  
    return sum((X.dot(thea)-Y)**2)/(2*m)  
  
#批梯度下降函数  
def batchgrad(data,label):  
    X = np.array(data)  
    m, n = np.shape(X)  
    Y = np.array(label).reshape(m,1)  
    alpha=0.01                   #定义步长  
    iterations = 1500;           #定义迭代次数  
    thea=np.ones((2,1))          #定义初始的点  
    for k in range(iterations):  
        H = X.dot(thea)  
        T = np.zeros((2, 1))  
        for i in range(m):  
           T=T+((H[i]-Y[i])*X[i]).reshape(2,1)  
        thea = thea - (alpha * T)/m  
    return thea  
  
#随机梯度下降函数  
def Randomgrad(data,label):  
    X = np.array(data)  
    m, n = np.shape(X)  
    Y = np.array(label).reshape(m,1)  
    alpha=0.01                   #定义步长  
    thea=np.ones((2,1))          #定义初始的点  
    for i in range(m):  
        thea=thea+alpha*((Y[i]-X[i].dot(thea))*X[i]).reshape(2,1)  
    return thea  
  
#最小二乘法  
def Leastsquares(data,label):  
    X = np.array(data)  
    m, n = np.shape(X)  
    Y = np.array(label).reshape(m, 1)  
    return np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y)  
  
if __name__=="__main__":  
    data,label=ReadFile('ex1data1.txt')  
    X = np.array(data)  
    #thea=batchgrad(data,label)  
    #thea=Randomgrad(data,label)  
    thea=Leastsquares(data,label)  
    print(thea)  
    Y=X.dot(thea)  
    fig=plt.figure()  
    ax=fig.add_subplot(111)  
    x=[]  
    y1=[]  
    y2=[]  
    for i in range(len(data)):  
        x.append(data[i][1])  
        y1.append(label[i])  
        y2.append(Y[i])  
    ax.scatter(x,y1,c='red')  
    ax.plot(x,y2)  
    plt.xlim(5,25)  
    plt.xlabel("X1")  
    plt.ylabel("X2")  
    plt.show()  
  