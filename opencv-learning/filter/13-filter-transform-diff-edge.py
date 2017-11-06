# -*- coding: utf-8 -*-
'''
平移和差边缘检测
'''

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('../datas/f1.png') #直接读为灰度图像
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img1 = np.float32(img) #转化数值类型
k1_3x3 = [
        [0,0,0],
        [-1,1,0],
        [0,0,0],
        ]
k2_3x3 = [
        [0,-1,0],
        [0, 1,0],
        [0,0,0],
        ]
k3_3x3 = [
        [-1,0,0],
        [0,1,0],
        [0,0,0],
        ]

k1 = np.array(k1_3x3,np.float32)
k2 = np.array(k2_3x3,np.float32) 
k3 = np.array(k1_3x3,np.float32)


dst1 = cv2.filter2D(img1,-1,k1)
dst2 = cv2.filter2D(img1,-1,k2)
dst3 = cv2.filter2D(img1,-1,k3)
#cv2.filter2D(src,dst,kernel,auchor=(-1,-1))函数：
#输出图像与输入图像大小相同
#中间的数为-1，输出数值格式的相同plt.figure()
plt.subplot(2,2,1),plt.imshow(np.uint8(img1),'gray')#默认彩色，另一种彩色bgr
plt.subplot(2,2,2),plt.imshow(np.uint8(dst1),'gray')
plt.subplot(2,2,3),plt.imshow(np.uint8(dst2),'gray')
plt.subplot(2,2,4),plt.imshow(np.uint8(dst3),'gray')
plt.show()

