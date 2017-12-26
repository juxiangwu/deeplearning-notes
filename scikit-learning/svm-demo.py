# -*- coding: utf-8 -*-

'''
加载数据
'''

import numpy as np
from sklearn import datasets
from sklearn import svm


iris = datasets.load_iris()
digits = datasets.load_digits()

clf = svm.SVC(gamma=0.001,C=100.0)

# 训练数据
clf.fit(digits.data[:-1],digits.target[:-1])

res = clf.predict(digits.data[-1:])
print(res)