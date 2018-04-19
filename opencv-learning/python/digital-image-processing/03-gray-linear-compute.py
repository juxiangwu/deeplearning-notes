# coding:utf-8
'''
灰度图像线性运算
公式：g(x,y) = p * f(x,y) + L
其中：f(x,y)为输入灰度图像像素值,g(x,y)为输出灰度图像像素值
参数：p = 1,L = 0,则复制图像；
      p > 1,则图像对比度减少
      p = 1,L!=0,则图像变亮
      p < 0,则图像变暗
'''

import cv2
import numpy as np

def grey_linear_compute(image,p,l):
    img_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    rows,cols = img_gray.shape
    dist = np.zeros_like(img_gray)

    for y in range(rows):
        for x in range(cols):
            pixel = img_gray[y,x]
            new_pixel = wise_element(p * pixel + l)
            dist[y,x] = new_pixel

    return dist


def rgb_linear_compute(image,p,l):
    # img_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    rows,cols,_ = image.shape
    dist = np.zeros_like(image)

    for y in range(rows):
        for x in range(cols):
            pixel = image_rgb[y,x]
            r = wise_element(p * pixel[0] + l)
            g = wise_element(p * pixel[1] + l)
            b = wise_element(p * pixel[2] + l)
            dist[y,x] = (b,g,r)
    return dist

def wise_element(value):
    dist = value
    if dist > 255:
        dist = 255
    if dist < 0:
        dist = 0
    return dist

src = cv2.imread('datas/l1.jpg')
gray = grey_linear_compute(src,1.1,10)
rgb = rgb_linear_compute(src,1.1,10)
cv2.imshow('src-rgb',src)
cv2.imshow('src-gray',cv2.cvtColor(src,cv2.COLOR_RGB2GRAY))
cv2.imshow('gray',gray)
cv2.imshow('rgb',rgb)

cv2.waitKey()
cv2.destroyAllWindows()
