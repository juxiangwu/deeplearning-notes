# -*- coding: utf-8 -*-
import sys,os
import jieba

# 设置UTF-8 Unicode环境
#reload(sys)
#sys.setdefaultencoding('utf-8')

seg_list = jieba.cut('小明1995年毕业于北京清华大学',cut_all=False)
for seg in seg_list:
    print(seg)
