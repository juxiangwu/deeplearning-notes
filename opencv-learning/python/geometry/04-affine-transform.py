#coding:utf-8
'''
仿射变换
'''

import cv2
import numpy as np

src = cv2.imread('datas/l1.jpg')

rows,cols,channel = src.shape


src_points = np.float32([[50,50],[200,50],[50,200]])  
dst_points =  np.float32([[10,100],[200,50],[100,250]])

warp_mat = cv2.getAffineTransform(src_points,dst_points)
dist_affine = cv2.warpAffine(src,warp_mat,(cols,rows))

rotate_map = cv2.getRotationMatrix2D((cols / 2,rows / 2),60,0.7)
dist_rotate = cv2.warpAffine(src,rotate_map,(cols,rows))

cv2.imshow('src',src)
cv2.imshow('affine transform',dist_affine)
cv2.imshow('rotate transform',dist_rotate)

cv2.waitKey()
cv2.destroyAllWindows()