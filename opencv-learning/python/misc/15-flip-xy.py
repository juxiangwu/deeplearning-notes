#coding:utf-8

'''
XY轴变换
'''

import numpy as np
import cv2

src = cv2.imread('datas/l1.jpg')
dst_y = np.zeros_like(src)
dst_x = np.zeros_like(src)
dst_xy = np.zeros_like(src)

rows,cols,channels = src.shape

for y in range(rows):
    for x in range(cols):
        dst_y[y,x] = src[rows - y - 1,x]
        dst_x[y,x] = src[y,cols - x - 1]
        dst_xy[y,x] = src[rows - y - 1,cols - x - 1]

cv2.imshow('src',src)
cv2.imshow('dst:y',dst_y)
cv2.imshow('dst:x',dst_x)
cv2.imshow('dst:xy',dst_xy)

cv2.waitKey()
cv2.destroyAllWindows()