# -*- coding: utf-8 -*-

'''
kNN分类算法
'''

import numpy as np 
import matplotlib.pyplot as plt 
import operator

def createDataSet():
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']

    return group,labels

k = 3

# 夹角余弦距离公式
def cosdist(vec1,vec2):
    return np.dot(vec1,vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))


def classify(testdata,traindata,listClasses,k):
    #返回样本集的行数
    dataSetSize = traindata.shape[0]
    distance = np.array(np.zeros(dataSetSize))
    for indx in range(dataSetSize):
        distance[indx] = cosdist(testdata,traindata[indx])
    
    # 根据生成的夹角余弦从大到小排序，结果为索引号
    sortedDistIndicies = np.argsort(-distance)
    classCount = {}

    for i in range(k):
        # 按排序顺序返回样本集对应的类别标签
        voteIlabel = listClasses[sortedDistIndicies]
        # 为字典classCount赋值，相同key,相同value 加1
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    # 对分类字典classCount按value重新排序
    sortedClassCount = sorted(data.iteritems(),key = operator.itemgetter(1),reverse = True)

    # 返回值最高的一项
    return sortedClassCount

dataset,labels = createDataSet()

testdata = [0.2,0.2]

# 绘图
fig = plt.figure()
ax = fig.add_subplot(111)
indx = 0

for point in dataset:
    if labels[indx] == 'A':
        ax.scatter(point[0],point[1],c='blue',marker='o',linewidths = 0,s = 300)
        plt.annotate("("+str(point[0])+",("+str(point[1])+")",xy=(point[0],point[1]))
    else:
        ax.scatter(point[0],point[1],c='red',marker='^',linewidths = 0,s = 300)
        plt.annotate("("+str(point[0])+",("+str(point[1])+")",xy=(point[0],point[1]))
    indx += 1

ax.scatter(testdata[0],testdata[1],c='red',marker='^',linewidths = 0,s = 300)
plt.annotate("("+str(testdata[0])+",("+str(testdata[1])+")",xy=(testdata[0],testdata[1]))

plt.show()