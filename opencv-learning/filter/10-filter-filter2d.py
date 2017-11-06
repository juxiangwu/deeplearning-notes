# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../datas/f1.png',0) #直接读为灰度图像
img1 = np.float32(img) #转化数值类型
kernel = np.ones((5,5),np.float32)/25
print(kernel)
dst = cv2.filter2D(img1,-1,kernel)
#cv2.filter2D(src,dst,kernel,auchor=(-1,-1))函数：
#输出图像与输入图像大小相同
#中间的数为-1，输出数值格式的相同plt.figure()
plt.subplot(1,2,1),plt.imshow(img1,'gray')#默认彩色，另一种彩色bgr
plt.subplot(1,2,2),plt.imshow(dst,'gray')
plt.show()