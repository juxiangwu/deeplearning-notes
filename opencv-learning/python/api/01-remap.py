#coding:utf-8
'''
图像重映射
'''
import cv2
import numpy as np

src = cv2.imread('datas/l1.jpg')
rows,cols,channels = src.shape

img_x = np.zeros((rows,cols),np.float32)
img_y = np.zeros((rows,cols),np.float32)

# 坐标映射
for y in range(rows):
    for x in range(cols):
        img_y[y,x] = rows - y
        img_x[y,x] = cols - x

dst = cv2.remap(src,img_x,img_y,cv2.INTER_LINEAR)

cv2.imshow('src',src)
cv2.imshow('dst',dst)

cv2.waitKey()
cv2.destroyAllWindows()