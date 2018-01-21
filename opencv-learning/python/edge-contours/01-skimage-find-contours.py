# -*- coding: utf-8 -*-
'''
使用skimage 查找轮廓
'''
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure,draw 
import cv2

#生成二值测试图像
img=np.zeros([100,100])
img[20:40,60:80]=1  #矩形
rr,cc=draw.circle(60,60,10)  #小圆
rr1,cc1=draw.circle(20,30,15) #大圆
img[rr,cc]=1
img[rr1,cc1]=1

src = cv2.imread('../datas/i3.png',0)
_,src = cv2.threshold(src,110,255,cv2.THRESH_BINARY)
#检测所有图形的轮廓
contours = measure.find_contours(np.uint8(src), 0.75)

#绘制轮廓
fig, (ax0,ax1) = plt.subplots(1,2,figsize=(8,8))
ax0.imshow(src,plt.cm.gray)
ax1.imshow(src,plt.cm.gray)
print(len(contours))
for n, contour in enumerate(contours):
    ax1.plot(contour[:, 1], contour[:, 0], linewidth=1)
ax1.axis('image')
ax1.set_xticks([])
ax1.set_yticks([])
plt.show()
