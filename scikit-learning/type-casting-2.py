# -*- coding: utf-8 -*-
'''
类型转换
'''

import numpy as np
from sklearn import datasets
from sklearn.svm import SVC

iris = datasets.load_iris()
clf = SVC()
clf.fit(iris.data,iris.target)

print(list(clf.predict(iris.data[:3])))
clf.fit(iris.data,iris.target_names[iris.target])
res = list(clf.predict(iris.data[:3]))
print(res)