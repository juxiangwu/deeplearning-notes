# -*- coding: utf-8 -*-
'''
线性模型
'''

from sklearn import datasets
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt

diabets = datasets.load_diabetes()
diabets_X_train = diabets.data[:-20]
diabets_X_test = diabets.data[-20:]
diabets_y_train = diabets.target[:-20]
diabets_y_test = diabets.target[-20:]

regr = linear_model.LinearRegression()
regr.fit(diabets_X_train,diabets_y_train)

print(regr.coef_)

res = np.mean((regr.predict(diabets_X_test) - diabets_y_test) ** 2)
print(res)

res = regr.score(diabets_X_test,diabets_y_test)
print('score:\n',res)

X = np.c_[0.5,1].T
y = [0.5,1]

test = np.c_[0,2].T
regr2 = linear_model.LinearRegression()
plt.figure()

np.random.seed(0)

for _ in range(6):
    this_X = 0.1 * np.random.normal(size=(2,1)) + X
    regr2.fit(this_X,y)
    plt.plot(test,regr2.predict(test))
    plt.scatter(this_X,y,s = 3)

plt.show()