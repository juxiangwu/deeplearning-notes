# -*- coding: utf-8 -*-
'''
高通滤波器
'''

import numpy as np
import cv2
from scipy import ndimage

kernel_3x3 = np.array([
        [-1,-1,-1],
        [-1, 8,-1],
        [-1,-1,-1]
        ])

kernel_5x5 = np.array([
        [-1,-1,-1,-1,-1],
        [-1, 1, 2, 1,-1],
        [-1, 2, 4, 2,-1],
        [-1, 1, 2, 1,-1],
        [-1,-1,-1,-1,-1],
        ])

img = cv2.imread('datas/f1.png',0)

k3 = ndimage.convolve(img,kernel_3x3)
k5 = ndimage.convolve(img,kernel_5x5)

blured = cv2.GaussianBlur(img,(11,11),0)
g_hpf = img - blured

cv2.imshow('HPF-3x3',k3)
cv2.imshow('HPF-5x5',k5)
cv2.imshow("HPF",g_hpf)
cv2.waitKey()
cv2.destroyAllWindows()