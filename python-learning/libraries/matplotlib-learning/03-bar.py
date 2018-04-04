#coding:utf-8
from matplotlib import pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

'''
数据取值分布
'''

grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)
plt.bar([x - 4 for x in histogram.keys()], # 每个条形向左侧移动4个单位
 histogram.values(), # 给每个条形设置正确的高度
 8) # 每个条形的宽度设置为8
plt.axis([-5, 105, 0, 5]) # x轴取值从-5到105
 # y轴取值0到5
plt.xticks([10 * i for i in range(11)]) # x轴标记为0，10，...，100
plt.xlabel("十分相")
plt.ylabel("学生数")
plt.title("考试分数分布图")
plt.show()