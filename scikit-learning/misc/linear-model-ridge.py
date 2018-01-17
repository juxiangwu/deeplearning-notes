# -*- coding: utf-8 -*-

'''
线性模型
'''

from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

regr = linear_model.Ridge()

X = np.c_[0.5,1].T
y = [0.5,1]
test = np.c_[0,2].T

plt.figure()

np.random.seed(0)

for _ in range(6):
    this_X = 0.1 * np.random.normal(size=(2,1)) + X
    regr.fit(this_X,y)
    plt.plot(test,regr.predict(test))
    plt.scatter(this_X,y,s = 3)

alphas = np.logspace(-4,-1,6)

plt.show()

