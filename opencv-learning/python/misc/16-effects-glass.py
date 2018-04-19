#coding:utf-8
'''
毛玻璃效果
'''

import cv2
import numpy as np

src = cv2.imread('datas/images/f1.jpg')
dst = np.zeros_like(src)

rows,cols,_ = src.shape
offsets = 5
random_num = 0

for y in range(rows - offsets):
    for x in range(cols - offsets):
        random_num = np.random.randint(0,offsets)
        dst[y,x] = src[y + random_num,x + random_num]

cv2.imshow('src',src)
cv2.imshow('dst',dst)

cv2.waitKey()
cv2.destroyAllWindows()