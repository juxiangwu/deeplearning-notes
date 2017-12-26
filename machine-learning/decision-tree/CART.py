# -*- coding: utf-8 -*-
'''
CART决策树
'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor

def plotfigure(X,X_test,y,yp):
    plt.figure()
    plt.scatter(X,y,c='k',label='data')
    plt.plot(X_test,yp,c='r',label='max_depth=5',linewidth=2)
    plt.xlabel('data')
    plt.ylabel('target')
    plt.title('Decistion Tree Regression')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    x = np.linspace(-5,5,200)
    siny = np.sin(x)
    X = np.mat(x).T
    y = siny + np.random.rand(1,len(siny)) * 1.5
   # y = y.tolist()

    # 声明CART
    clf = DecisionTreeRegressor(max_depth=4)
    #clf.fit(X,y)
    print(y.shape,X.shape)
    # 训练CART
    clf.fit(X,y)

    # 预测
    X_test = np.arange(-5.,5,0.05)[:,np.newaxis]
    yp = clf.predict(X_test)

    plotfigure(X,X_test,y,yp)
