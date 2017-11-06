# -*- coding: utf-8 -*-
'''
均值滤波
'''
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('../datas/f1.png',0) #直接读为灰度图像
blur = cv2.blur(img,(3,5))#模板大小3*5
plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
plt.subplot(1,2,2),plt.imshow(blur,'gray')
plt.show()
