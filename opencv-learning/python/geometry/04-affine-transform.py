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

# 仿射变换
warp_mat = cv2.getAffineTransform(src_points,dst_points)
dist_affine = cv2.warpAffine(src,warp_mat,(cols,rows))

# 旋转
rotate_mat = cv2.getRotationMatrix2D((cols / 2,rows / 2),60,0.7)
dist_rotate = cv2.warpAffine(src,rotate_mat,(cols,rows))

# 平移
translation_mat = np.array([[1,0,100],[0,1,50]],dtype=np.float32)
dist_translation = cv2.warpAffine(src,translation_mat,(rows+200,cols+200),borderValue=(155, 155, 155))

# 投影
pts1 = np.float32( [ [56,65],[368,52],[28,387],[389,390] ] )  
pts2 = np.float32( [ [0,0],[300,0],[0,300],[300,300] ] )  
M = cv2.getPerspectiveTransform(pts1 , pts2)  
dist_projective = cv2.warpPerspective(src,M,(cols,rows))

cv2.imshow('src',src)
cv2.imshow('affine transform',dist_affine)
cv2.imshow('rotate transform',dist_rotate)
cv2.imshow('translation',dist_translation)
cv2.imshow('projective',dist_projective)

cv2.waitKey()
cv2.destroyAllWindows()