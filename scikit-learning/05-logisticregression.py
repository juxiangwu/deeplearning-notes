# -*- coding:utf-8 -*-

import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model

iris = datasets.load_iris()

iris_X = iris.data
iris_y = iris.target

indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]

logistic = linear_model.LogisticRegression(C=1e5)

logistic.fit(iris_X_train,iris_y_train)

