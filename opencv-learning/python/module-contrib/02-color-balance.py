#coding:utf-8

'''
色彩均衡
'''

import cv2

src = cv2.imread('datas/images/f1.jpg')

# 黑白平衡
inst = cv2.xphoto.createGrayworldWB()
inst.setSaturationThreshold(0.95)
grayworld = inst.balanceWhite(src)

cv2.imshow('src',src)
cv2.imshow('balance-white',grayworld)

cv2.waitKey()
cv2.destroyAllWindows()

