# -*- coding: utf-8 -*-
'''
scikit-learn ID3决策树
'''
import numpy as np
from sklearn import tree 
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.cross_validation import train_test_split

#数据读入
data = []
labels = []

with open('datas/thin-fat-datas.dat') as ifile:
    for line in ifile:
        tokens = line.strip().split(',')
        data.append([float(tk) for tk in tokens[:-1]])
        labels.append(tokens[-1])

x = np.array(data)
labels = np.array(labels)
y = np.zeros(labels.shape)

#标签转化为0,1
y[labels == 'fat'] = 1

# 拆分训练数据和测试数据
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2)

#使用信息熵作为划分标准,对决策树进行训练
clf = tree.DecisionTreeClassifier(criterion="entropy")
print(clf)

clf.fit(x_train,y_train)

#把决策树写入文件
with open('datas/tree.dot','w') as f:
    f = tree.export_graphviz(clf,out_file=f)

print(clf.feature_importances_)

answer = clf.predict(x_train)
print(answer)

precision,recall,threshold = precision_recall_curve(y_train,clf.predict(x_train))
