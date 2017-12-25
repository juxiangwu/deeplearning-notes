# -*- coding: utf-8 -*-

'''
树与分类结构的可视化
'''
import numpy as np 
import sys
import matplotlib.pyplot as plt 
import treePlotter as tp 

# 配置UTF-8输出环境
reload(sys)

sys.setdefaultencoding('utf-8')

# 绘制树
myTree = {'root' :
            {0:'leaf node',
            1:{'level 2':{0:'leaf node',1:'leafnode'}},2:{'level2':{0:'leaf node',1:'leaf node'}}}}

tp.createPlot(myTree)