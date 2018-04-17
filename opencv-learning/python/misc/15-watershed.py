#coding:utf-8
'''
图像分割
'''

import cv2
import numpy as np
import os

img = cv2.imread('datas/examples.png')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
 
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
# 膨胀
sure_bg = cv2.dilate(opening,kernel,iterations=3)

# 计算二值图象中所有像素离其最近的值为0像素的近似距离
dist_transform = cv2.distanceTransform(opening,1,5)
ret, sure_fg = cv2.threshold(dist_transform,0.2*dist_transform.max(),255,0)
# 查找不确定区域
sure_fg = np.uint8(sure_fg)
# 前景消除
unknown = cv2.subtract(sure_bg,sure_fg)
 
cv2.imshow('image',sure_fg)
cv2.waitKey(0)