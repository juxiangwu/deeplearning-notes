#coding:utf-8
'''
Schmid滤波
参考：https://blog.csdn.net/xiaowei_cqu/article/details/25131473
'''
import cv2
import numpy as np
import math

def schmid_kernel(tao,sigma):
    r = float(sigma / (4.0 * tao))
    sigma2 = float(sigma * sigma)

    half_filter_size = 10
    filter_size = half_filter_size * 2 + 1

    schmid = np.zeros((filter_size,filter_size),np.float32)
    filter_sum = 0.0
    for i in range(filter_size):
        #s = schmid[i,:]
        for j in range(filter_size):
            x = i - half_filter_size
            y = j - half_filter_size

            r = math.sqrt(x * x + y * y)

            tmp = 2.0 * math.pi * tao * r / sigma
            tmp2 = float(r * r / (2.0 * sigma2))

            schmid[i,j] = math.cos(tmp) * math.exp(-tmp2)
            filter_sum += schmid[i,j]
    
    if np.abs(filter_sum - 0.0) < 1e-6:
        return schmid
    
    for i in range(filter_size):
        #s = schmid[i,:]
        for j in range(filter_size):
            schmid[i,j] /= filter_sum
    
    return schmid

def schmid_filter(img,tao,sigma):
    kernel = schmid_kernel(tao,sigma)
    
    kernel_height = kernel.shape[0]
    kernel_width = kernel.shape[1]

    conv_height = img.shape[0] - kernel_height + 1
    conv_width = img.shape[1] - kernel_width + 1

    conv_img = np.zeros((conv_height,conv_width),dtype=np.uint8)

    for i in range(conv_height):
        for j in range(conv_width):
            conv_img[i][j] = wise_element_sum(img[i:i + kernel_height,j:j + kernel_width],kernel)

    return conv_img

def wise_element_sum(img,kernel):

    res = (img * kernel).sum()

    if res < 0:
        res = 0
    elif res > 255:
        res = 255
    return res
        


src = cv2.imread('datas/face.jpg')
kernel = schmid_kernel(4,2)
# print('kernel = \n',kernel)
dist = np.zeros_like(src)
cv2.filter2D(src, -1, kernel, dist)
conv_img_r = schmid_filter(src[:,:,0],4,2)
conv_img_g = schmid_filter(src[:,:,1],4,2)
conv_img_b = schmid_filter(src[:,:,2],4,2)

rgb = [conv_img_r,conv_img_g,conv_img_b]
conv_img = cv2.merge(rgb)

cv2.imshow('src',src)
cv2.imshow('dst:filter2D',dist)
cv2.imshow('dst:convd:',conv_img)

cv2.waitKey()
cv2.destroyAllWindows()