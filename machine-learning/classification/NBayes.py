# -*- coding: utf-8 -*-

'''
朴素贝叶斯分类
'''

class NBayes(object):
    def __init__(self):
        self.vocabulary = []
        self.idf = 0
        self.tf = 0
        self.tdm = 0
        self.Pcates = {}
        self.labels = []
        self.doclength = 0
        self.vocablen = 0
        self.testset = 0

    # 导入和训练数据，生成算法必要的参数和数据结构
    def train_set(self,trainset,classVec):
        sefl.cate_prob(classVec)
        self.doclength = len(trainset)
        tempset = set()
        # 生成词典
        [tempset.add(word) for doc in trainset for word in doc] 
        self.vocabulary = list(tempset)
        self.vocablen = len(self.vocabulary)
        self.calc_wordfreq(trainset)
        self.build_tdm()
    
    # 计算在数据集中每个分类的概率
    def cate_prob(self,classVec):
        self.labels = classVec
        # 获取全部分类
        labeltemps = set(self.labels)

        for labeltemp in labeltemps:
            # 统计列表中重复的分类
            self.Pcates[labeltemp] = float(self.labels.count(labeltemp)) / float(len(self.labels))

    #生成普通的词频向量
    def calc_wordfreq(self,trainset):
        self.idf = np.zeros([1,self.vocablen])
        self.tf = np.zeros([self.doclength,self.vocablen])

        for indx in range(self.doclength):
            for word in trainset[indx]:
                #找到文本在词字典中的位置+1
                self.tf[indx,self.vocabulary.index(word)] += 1

            for signleword in set(trainset[indx])
                self.idf[0,self.vocabulary,index(signleword)] += 1  
    
    # 按分类累计向量空间的每维值P(x|y(i))
    def build_tdm(self):
        self.tdm = np.zeros([len(self.Pcates),self.vocablen])
        sumlist = np.zeros([len(self.Pcates),1])

        for indx in range(self.doclength):
            # 将同一类别的词向量空间值加总
            self.tdm[self.labels[indx]] += self.tf[indx]

            # 统计每个分类的总值
            sumlist[self.labels[indx]] = np.sum(self.tdm[self.labels[indx]])
        self.tdm = self.tdm / sumlist

        #将测试集映射到当前词典
        def map2vocab(self,testdata):
            self.testset = np.zeros([1,self.vocablen])
            for word in testdata:
                self.testset[0,self.vocabulary.index(word)] += 1
        
        # 预测分类结果
        def predict(self,testset):
            if np.shape(testset)[1] != self.vocablen:
                print('invalid input')
                exit(0)
            predvalue = 0
            preclass = ""
            for tdm_vect,keyclass in zip(self.tdm,self.Pcates):
                # P(x|yi) P(yi)
                #计算最大分类值
                temp = np.sum(testset * tdm_vect * self.Pcates[keyclass])
                if temp > predvalue:
                    predvalue = temp
                    preclass = keyclass
            return predclass