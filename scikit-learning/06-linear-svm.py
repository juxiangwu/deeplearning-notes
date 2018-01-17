# -*- coding:utf-8 -*-

# Linear SVMs

from sklearn import svm
from sklearn import datasets

diabetes = datasets.load_diabetes()
diabetes_X_train = diabetes.data[:-20]
diabetes_X_test = diabetes.data[-20:]
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

svc = svm.SVC(kernel='linear')

svc.fit(diabetes_X_train,diabetes_y_train)
print(svc)

svc = svm.SVC(kernel='poly',degree=3)
print(svc)

svc = svm.SVC(kernel='rbf')
print(svc)