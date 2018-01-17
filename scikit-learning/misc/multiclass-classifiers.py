# -*- coding: utf-8 -*-

'''
多分类
'''
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer
from sklearn.preprocessing import MultiLabelBinarizer

X = [[1,2],[2,4],[4,5],[3,2],[3,1]]
y = [0,0,1,1,2]

classif = OneVsRestClassifier(estimator = SVC(random_state=0))
classif.fit(X,y)
res = classif.predict(X)
print(res)

y = LabelBinarizer().fit_transform(y)
classif.fit(X,y)
res = classif.predict(X)
print(res)

y1 = [[0,1],[0,2],[1,3],[0,2,3],[2,4]]
y1 = MultiLabelBinarizer().fit_transform(y1)
classif.fit(X,y1)
res = classif.predict(X)
print(res)

