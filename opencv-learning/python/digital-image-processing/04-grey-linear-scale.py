#coding:utf-8
'''
灰度拉伸
定义：灰度拉伸，也称对比度拉伸，是一种简单的线性点运算。作用：扩展图像的
      直方图，使其充满整个灰度等级范围内
公式：
g(x,y) = 255 / (B - A) * [f(x,y) - A],
其中，A = min[f(x,y)],最小灰度级；B = max[f(x,y)],最大灰度级；
     f(x,y)为输入图像,g(x,y)为输出图像

缺点：如果灰度图像中最小值A=0，最大值B=255，则图像没有什么改变

'''

import cv2
import numpy as np

def grey_scale(image):
    img_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    
    rows,cols = img_gray.shape
    flat_gray = img_gray.reshape((cols * rows,)).tolist()
    A = min(flat_gray)
    B = max(flat_gray)
    print('A = %d,B = %d' %(A,B))
    output = np.uint8(255 / (B - A) * (img_gray - A) + 0.5)
    return output

src = cv2.imread('datas/f4.jpg')
result = grey_scale(src)
cv2.imshow('src',cv2.cvtColor(src,cv2.COLOR_BGR2GRAY))
cv2.imshow('result',result)

cv2.waitKey()
cv2.destroyAllWindows()