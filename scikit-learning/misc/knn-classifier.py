# -*- coding: utf-8 -*-

'''
KNN分类器
'''

import numpy as np
from sklearn import datasets

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

iris_y2 = np.unique(iris_y)
print(iris_y2)

np.random.seed(0)

indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test  = iris_X[indices[-10:]]
iris_y_test  = iris_y[indices[-10:]]

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(iris_X_train,iris_y_train)

res = knn.predict(iris_X_test)
print(res)
print(iris_y_test)
