#coding:utf-8
'''
直方图均衡化
作用：通常用来增加图像局部对比度，尤其在图像的有用数据的对比度相当
      接近时，通过直方图均衡化，图像的亮度可以更好地在直方图上分布
基本思想：把原始图像的直方图变换为均匀分布的形式，增加了像素
        灰度值的动态范围，从而增强图像的整体对比度效果

算法实现步骤：
1、计算图像f的各个灰度级中像素出现的概率
  p(i) = n(i) / n ,{i|0,1,...,L - 1}
  其中：n(i)表示灰度级i出现的次数,L是图像中所有的灰度数,p实际上是图像的
        直方图归一化到0~1范围内，如果把c作为对应p的累计概率函数，则定义为：
               i
        c(i) = ∑(p(x(j))
               j=0
        c是图像的累计归一化直方图

2、创建一个形式为 y = T(x)的变化，原始图像中的每个值就生产一个y,这样
    y的累计概率函数形式就可以在所有值范围内进行线性化，转换公式为：
    y(i) = T(x(i)) = c(i)
'''

import cv2
import numpy as np

def hist_eq(image):
    img_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    rows,cols = img_gray.shape
    gray_flat = img_gray.reshape((rows*cols,))
    dist_flat = np.zeros_like(gray_flat)

    count_pixel = np.zeros((256,),np.int32)
    temp = np.zeros((256,),np.int32)
    pixmap = np.zeros((256,),np.uint8)
    image_bytes = cols * rows
    # 计算各个灰度级数量
    for index,value in enumerate(gray_flat):
        count_pixel[value] += 1

    # 计算灰度级的累计分布
    for i in range(256):
        if i == 0:
            temp[0] = count_pixel[0]
        else:
            temp[i] = temp[i - 1] + count_pixel[i]

        # 计算累计概率函数，并把值扩展到0~255
        value = 255.0 * (temp[i] / image_bytes)
        if value > 255:
            value = 255
        if value < 0:
            value = 0
        pixmap[i] = value

    # 灰度等级映射转换
    for i in range(image_bytes):
        dist_flat[i] = pixmap[gray_flat[i]]

    dist = dist_flat.reshape((rows,cols))

    return dist

src = cv2.imread('datas/l1.jpg')
gray = cv2.cvtColor(src,cv2.COLOR_RGB2GRAY)

dist = hist_eq(src)

# 调用OpenCV函数
dist_cv = np.zeros_like(gray)
cv2.equalizeHist(gray,dist_cv)

cv2.imshow('src',gray)
cv2.imshow('dist',dist)
cv2.imshow('opencv-histeq',dist_cv)
cv2.waitKey()
cv2.destroyAllWindows()
