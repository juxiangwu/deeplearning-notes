#coding:utf-8
__author__ = 'https://github.com/juxiangwu'
__version__ = '0.0.0.1'
__date__ = '2018-04-12'
'''
检测目标指定颜色
'''

import cv2
import numpy as np
import time

img = cv2.imread('datas/examples.png')
kernel_2x2 = np.ones((2,2),np.uint8)
kernel_3x3 = np.ones((3,3),np.uint8)
kernel_4x4 = np.ones((4,4),np.uint8)

if type(img) is None:
    print('cannot read image')
    exit(0)

# 转换成HSV图像
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower = np.array([20,20,20])
upper = np.array([30,255,255])

# 过滤[lower,upper]之外的颜色
mask = cv2.inRange(hsv,lower,upper)
cv2.imshow('mask',mask)
erosion = cv2.erode(mask,kernel_4x4,iterations = 1)
erosion = cv2.erode(erosion,kernel_4x4,iterations = 1)
dilation = cv2.dilate(erosion,kernel_4x4,iterations = 1)
dilation = cv2.dilate(dilation,kernel_4x4,iterations = 1)
# 保留目标颜色
target = cv2.bitwise_and(img, img, mask=dilation)
ret, binary = cv2.threshold(dilation,127,255,cv2.THRESH_BINARY) 

# 查找轮廓
image,contours,hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# 绘制轮廓

cv2.drawContours(img,contours,-1,(0,0,255),3)  
cv2.imshow('image',img)

cv2.waitKey()
cv2.destroyAllWindows()