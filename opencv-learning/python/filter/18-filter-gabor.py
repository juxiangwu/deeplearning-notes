#coding:utf-8

'''
Gabor滤波器参数可视化
'''

import cv2
import numpy as np
import math

# λ（波长）变化
kernel1 = cv2.getGaborKernel((311,311),10,0,5,0.5,0)
kernel2 = cv2.getGaborKernel((311,311),10,0,10,0.5,0)
kernel3 = cv2.getGaborKernel((311,311),10,0,15,0.5,0)
kernel4 = cv2.getGaborKernel((311,311),10,0,20,0.5,0)

cv2.imshow("lambda: 5", kernel1)
cv2.imshow("lambda: 10", kernel2)
cv2.imshow("lambda: 15", kernel3)
cv2.imshow("lambda: 20", kernel4)

# θ变化
kernel1 = cv2.getGaborKernel((311, 311), 10, 0, 10, 0.5, 0)
kernel2 = cv2.getGaborKernel((311, 311), 10, math.pi * 0.25, 10, 0.5)
kernel3 = cv2.getGaborKernel((311, 311), 10, math.pi * 0.5, 10, 0.5, 0)
kernel4 = cv2.getGaborKernel((311, 311), 10, math.pi * 0.75, 10, 0.5, 0)

cv2.imshow("theta: 0", kernel1)
cv2.imshow("theta: 45", kernel2)
cv2.imshow("theta: 90", kernel3)
cv2.imshow("theta: 135", kernel4)

# ψ的变化
kernel1 = cv2.getGaborKernel((311, 311), 5, 0, 10, 0.5, -180)
kernel2 = cv2.getGaborKernel((311, 311), 10, 0, 10, 0.5, -90)
kernel3 = cv2.getGaborKernel((311, 311), 15, 0, 10, 0.5, 90)
kernel4 = cv2.getGaborKernel((311, 311), 20, 0, 10, 0.5, 180)
cv2.imshow(u"ψ: -180", kernel1)
cv2.imshow(u"ψ: -90", kernel2)
cv2.imshow(u"ψ: 90", kernel3)
cv2.imshow(u"ψ: 180", kernel4)

# σ的变化：
kernel1 = cv2.getGaborKernel((311, 311), 5, 0, 10, 0.5, 0)
kernel2 = cv2.getGaborKernel((311, 311), 10, 0, 10, 0.5, 0)
kernel3 = cv2.getGaborKernel((311, 311), 15, 0, 10, 0.5, 0)
kernel4 = cv2.getGaborKernel((311, 311), 20, 0, 10, 0.5, 0)

cv2.imshow("sigma: 5", kernel1)
cv2.imshow("sigma: 10", kernel2)
cv2.imshow("sigma: 15", kernel3)
cv2.imshow("sigma: 20", kernel4)

# γ的变化

kernel1 = cv2.getGaborKernel((311, 311), 10, 0, 10, 0.5, 0)
kernel2 = cv2.getGaborKernel((311, 311), 10, 0, 10, 1.0, 0)
kernel3 = cv2.getGaborKernel((311, 311), 10, 0, 10, 1.5, 0)
kernel4 = cv2.getGaborKernel((311, 311), 10, 0, 10, 2.0, 0)
cv2.imshow("gamma: 0.5", kernel1)
cv2.imshow("gamma: 1.0", kernel2)
cv2.imshow("gamma: 1.5", kernel3)
cv2.imshow("gamma: 2.0", kernel4)

cv2.waitKey()
cv2.destroyAllWindows()