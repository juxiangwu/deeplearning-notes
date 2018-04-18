#coding:utf-8
'''
图像平移
'''

import numpy as np
import cv2

image = cv2.imread('datas/l1.jpg')

# 大小不改变，相当剪裁
def transform_without_change_size(image,xoffset,yoffset):
    rows = image.shape[0]
    cols = image.shape[1]

    dist = np.zeros_like(image)

    for y in range(rows):
        for x in range(cols):
            new_x = x - xoffset
            new_y = y - yoffset

            if new_x >=0 and new_y >= 0 and new_x < cols and new_y < rows:
                dist[y,x] = image[new_y,new_x] 

    return dist

# 大小改变
def transform_with_change_size(image,xoffset,yoffset):
    rows = image.shape[0] + np.abs(yoffset)
    cols = image.shape[1] + np.abs(xoffset)

    dist = np.zeros((rows,cols,image.shape[2]),image.dtype)

    for y in range(rows):
        for x in range(cols):
            new_x = x - xoffset
            new_y = y - yoffset

            if new_x >=0 and new_y >= 0 and new_x < cols and new_y < rows:
                dist[y,x] = image[new_y,new_x] 
    return dist


result = transform_without_change_size(image,50,50)
result2 = transform_with_change_size(image,100,100)
cv2.imshow('src',image)
cv2.imshow('dist',result)
cv2.imshow('dist2',result2)

cv2.waitKey()
cv2.destroyAllWindows()