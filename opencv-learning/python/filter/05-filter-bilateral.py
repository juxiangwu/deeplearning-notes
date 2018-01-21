# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('../datas/f1.png') #直接读为灰度图像
for i in range(2000): #添加点噪声
    temp_x = np.random.randint(0,img.shape[0])
    temp_y = np.random.randint(0,img.shape[1])
    img[temp_x][temp_y] = 255

#9---滤波领域直径
#后面两个数字：空间高斯函数标准差，灰度值相似性标准差

blur = cv2.bilateralFilter(img,9,75,75)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
blur = cv2.cvtColor(blur,cv2.COLOR_BGR2RGB)

plt.subplot(1,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
plt.subplot(1,2,2),plt.imshow(blur,'gray')
plt.show()