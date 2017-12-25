# -*- coding: utf-8 -*-
'''
ID3决策树
'''
import numpy as np
import math
import copy
import pickle

class ID3Tree(object):
    def __init__(self):
        self.tree = {}
        self.dataSet = []
        self.labels = []

    # 导入数据
    def loadDataSet(self,path,labels):
        recordlist = []
        fp = open(path,'r')
        content = fp.read()
        rowlist = content.splitlines()
        recordlist = [row.split('\t') for row in rowlist if row.strip()]
        self.dataSet = recordlist
        self.labels = labels
        #print(self.dataSet)
        
    # 执行决策树函数
    def train(self):
        labels = copy.deepcopy(self.labels)
        self.tree = self.buildTree(self.dataSet,labels)

    # 构建决策树
    def buildTree(self,dataSet,labels):
        cateList = [data[-1] for data in dataSet]
        # 程序终止条件1：如果classList只有一种决策标签，则停止划分，直接返回标签
        if cateList.count(cateList[0]) == len(cateList):
            return cateList[0]
        # 程序终止条件2：如果数据集的第一个决策标签只有一个，则返回该决策标签
        if len(dataSet[0]) == 1:
            return self.maxCate(cateList)

        # 核心算法
        bestFeat = self.getBestFeat(dataSet)
        bestFeatLabel = labels[bestFeat]

        tree = {bestFeatLabel:{}}
        del(labels[bestFeat])

        # 抽取最优特征的列向量
        uniqueVals = set([data[bestFeat] for data in dataSet])
        for value in uniqueVals:
            subLabels = labels[:]

            # 按最优特征列和值分隔数据集
            splitDataset = self.splitDataset(dataSet,bestFeat,value)
            subTree = self.buildTree(splitDataset,subLabels)
            tree[bestFeatLabel][value] = subTree
        return tree

    # 计算出现类别最多的标签
    def maxCate(self,catelist):
        items = dict([(catelist.count(i),i) for i in catelist])
        return items[max(items)]
    
    # 计算最优特征
    def getBestFeat(self,dataSet):
        # 计算特征向量，其中最后一列用于类别标签，因此要减去
        numFeatures = len(dataSet[0]) - 1
        #数据源的香农熵
        baseEntropy = self.computeEntropy(dataSet)
        bestInfoGain = 0.0 #最优的信息增益
        bestFeature = -1
        for i in range(numFeatures):
            uniqueVals = set([data[i] for data in dataSet])
            newEntropy = 0.0
            for value in uniqueVals:
                # 按选定列i和唯一值分隔数据值
                subDataSet = self.splitDataset(dataSet,i,value)
                prob = len(subDataSet) / float(len(dataSet))
                newEntropy += prob * self.computeEntropy(subDataSet)
            # 计算最大增益
            infoGain = baseEntropy - newEntropy
            if (infoGain > bestInfoGain):
                bestInfoGain = infoGain
                bestFeature = i
        return bestFeature

    # 计算信息熵
    def computeEntropy(self,dataSet):
        datalen = float(len(dataSet))
        cateList = [data[-1] for data in dataSet]

        # 得到类别为key，出现次数value的字典
        items = dict([(i,cateList.count(i)) for i in cateList])
        infoEntropy = 0.0
        for key in items:
            prob = float(items[key]) / datalen
            infoEntropy -= prob * math.log(prob,2)

        return infoEntropy

    # 划分数据集
    def splitDataset(self,dataSet,axis,value):
        rtnList = []
        for featVec in dataSet:
            if featVec[axis] == value:
                rFeatVec = featVec[:axis]
                rFeatVec.extend(featVec[axis+1:])
                rtnList.append(rFeatVec)
        return rtnList
    
    # 持久化决策树
    def storeTree(self,inputTree,filename):
        fw = open(filename,'w')
        pickle.dump(inputTree,fw)
        fw.close()

    # 从持久化文件加载决策树
    def loadTree(self,filename):
        fr = open(filename,'r')
        return pickle.load(fr)

    # 决策树分类
    def predict(self,inputTree,featLabels,testVec):
        
        root = list(inputTree.keys())[0]
        secondDict = inputTree[root]
        featIndex = featLabels.index(root)
        key = testVec[featIndex]
        valueOfFeat = secondDict[key]
        if isinstance(valueOfFeat,dict):
            classLabel = self.predict(valueOfFeat,featLabels,testVec)
        else:
            classLabel = valueOfFeat
        return classLabel
        
        

if __name__ == '__main__':
    
    dtree = ID3Tree()
    dtree.loadDataSet('datas/id3-dataset.dat',['age','revenue','student','credit'])
    dtree.train()
    print('ID3 tree structure:\n',dtree.tree)

    labels = ['age','revenue','student','credit']
    vector = ['0','1','0','0']
    res = dtree.predict(dtree.tree,labels,vector)
    print('predict result:\n',res)