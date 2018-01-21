# -*- coding: utf-8 -*-
'''
使用sigmoid函数对图片像素操作
'''

import cv2
import numpy as np

def sigmoid(inX):
     return np.longfloat(1.0/(1 + np.exp(-inX)))


img = cv2.imread('../datas/f1.png')

cv2.imshow("Image",img)

dst = sigmoid(img / 255) 

cv2.imshow("dst",dst)

cv2.waitKey()
cv2.destroyAllWindows()