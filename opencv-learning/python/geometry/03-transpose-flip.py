#coding:utf-8
'''
图像翻转
'''

import numpy as np
import cv2

src = cv2.imread('datas/l1.jpg')

# 逆时针旋转90度
result = cv2.transpose(src)

# 垂直翻转
result2 = cv2.flip(src,0)

# 水平翻转
result3 = cv2.flip(src,1)
cv2.imshow('src',src)
cv2.imshow("transpose",result)
cv2.imshow('flip:0',result2)
cv2.imshow('flip:1',result3)

cv2.waitKey()
cv2.destroyAllWindows()