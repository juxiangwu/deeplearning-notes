#coding:utf-8

'''
图像灰度化
1、基本公式：Gray(i,j) = [R(i,j) + G(i,j) + B(i,j)] / 3
根据人眼对颜色的感知程度不同，衍生出第二个公式：
Gray(i,j) = 0.299 * R(i,j) + 0.587 * G(i,j) + 0.114 * B(i,j)
'''
import numpy as np
import cv2

def grey_avg2(image):
    
    img_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    rows,cols,_ = image.shape
    dist = np.zeros((rows,cols),dtype=image.dtype)
    
    for y in range(rows):
        for x in range(cols):
            r,g,b = img_rgb[y,x]
            r = np.uint8(r * 0.299)
            g = np.uint8(g * 0.587)
            b = np.uint8(b * 0.114)

            rgb = np.uint8(r * 0.299 + b * 0.114 + g * 0.587)
            dist[y,x] = rgb
    return dist


def grey_avg(image):
    img_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    rows,cols,_ = image.shape
    dist = np.zeros((rows,cols),dtype=image.dtype)
    
    for y in range(rows):
        for x in range(cols):
            avg = sum(image[y,x]) / 3
            dist[y,x] = np.uint8(avg)
    
    return dist

src = cv2.imread('datas/l1.jpg')

avg1 = grey_avg(src)
avg2 = grey_avg2(src)

cv2.imshow('src',src)
cv2.imshow('avg-1',avg1)
cv2.imshow('avg-2',avg2)

cv2.waitKey()
cv2.destroyAllWindows()
