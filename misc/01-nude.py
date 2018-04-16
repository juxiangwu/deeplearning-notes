#coding:utf-8
'''
基于肤色的裸体图像检测
'''
import nude
from nude import Nude

print(nude.is_nude('datas/images/test2.jpg'))

n = Nude('datas/images/test2.jpg')
n.parse()
print("damita :", n.result, n.inspect())