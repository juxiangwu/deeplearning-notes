# coding:utf-8
from matplotlib import pyplot as plt
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

years = [1950,1960,1970,1980,1990,2000,2010]
gdp = [300.2,543.3,1075.9,2862.5,5979.6,10289.7,14958.3]

plt.plot(years,gdp,color='green',marker='o',linestyle='solid')
plt.title(u'名义GDP')
plt.ylabel(u'十亿美元')
plt.show()