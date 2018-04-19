#coding:utf-8

'''
RGB图像底片效果
'''

import cv2
import numpy as np

src = cv2.imread('datas/l1.jpg')

dist = 255 - src

cv2.imshow('src',src)
cv2.imshow('dist',dist)

cv2.waitKey()
cv2.destroyAllWindows()