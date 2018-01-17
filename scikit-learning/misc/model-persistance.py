# -*- coding: utf-8 -*-
'''
模型持久化
'''

from sklearn import svm
from sklearn import datasets
from sklearn.externals import joblib
import pickle

clf = svm.SVC()
iris = datasets.load_iris()
X,y = iris.data,iris.target

clf.fit(X,y)

# 将模型序列化到文件
fw = open('temp/iris-svm.model','wb')
pickle.dump(clf,fw)
fw.close()

# 从文件加载模型
lf = open('temp/iris-svm.model','rb')
model = pickle.load(lf)
lf.close()

# 预测
res = model.predict(X[0:1])
print(res)

# 使用joblib
joblib.dump(clf,'temp/iris-svm.pkl')
pkl = joblib.load('temp/iris-svm.pkl')
res = pkl.predict(X[0:1])
print(res)