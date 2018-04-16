#coding:utf-8
'''
基于pHash感知哈希算法的物体跟踪
'''

import cv2
import numpy as np
import math
from scipy.fftpack import dct  

cur_x,cur_y,rect_x,rect_y,rect_width,rect_height = 0,0,0,0,0,0
drawing_box = False
gotBB = False

frame = None

def mouse_handler(event,x,y,flags,params):
    global cur_x,cur_y,rect_x,rect_y,rect_width,rect_height,drawing_box,gotBB
    if event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):
        print('mouse move:%d,%d,%d,%d' %(rect_x,rect_y,rect_width,rect_height))
        if drawing_box:
            cur_x = x
            cur_y = y
            rect_width = np.abs(x - rect_x)
            rect_height = np.abs(y - rect_y)

    elif event == cv2.EVENT_LBUTTONDOWN:
        print('mouse left button down:%d,%d',(x,y))
        drawing_box = True
        cur_x = x
        cur_y = y
        rect_x = x
        rect_y = y
        rect_width = 0
        rect_height = 0

    elif event == cv2.EVENT_LBUTTONUP:
        print('mouse left button up')
        drawing_box = False
        cur_x = x
        cur_y = y
        rect_width = np.abs(cur_x - rect_x)
        rect_height = np.abs(cur_y - rect_y)

        gotBB = True


def cal_hashcode(image):
    dist = cv2.resize(image,(8,8))
    img_mean = cv2.mean(dist)
    return (dist > img_mean[0])

def cal_phashcode2(im):
        if im is None:  
            return 0  
        if len(im.shape) == 3 and im.shape[-1] == 3:  
            im = cv2.cvtColor(im,cv2.COLOR_RGB2GRAY) 
        im = im.astype(float)  
        im = cv2.resize(im, (32, 32))  
        
        dim = dct(im)  
        mean = np.sum(dim) / (32. * 32.)  
        val = 0  
        k = 0  
        for i in range(0, 8):  
            for j in range(0, 8):  
                if dim[i, j] > mean:  
                    val |= (1 << k)  
                k += 1  
        return val  

def cal_phashcode(image):
    if image is None:
        return 0
    if len(image.shape) == 3 and image.shape[-1] == 3:
        image = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    dist = cv2.resize(image,(32,32))
    float_image = np.float32(dist)
    image_dct = cv2.dct(float_image)
    image_mean = cv2.mean(image_dct[0:8,0:8])
    # return (image_dct[0:8,0:8] > image_mean[0])
    value = 0
    k = 0
    for i in range(8):
        for j in range(8):
            if image_dct[i,j] > image_mean[0]:
                value |= (1 << k)
            k += 1
    return value

def hamming(a, b):  
        def x32(x):  
            a = 0xff+(0xff<<8);  
            b = a^(a << 8);  
            c = b^(b << 4);  
            d = c^(c << 2);  
            e = d^(d << 1);  
            x = (x&e)+((x >> 1)&e);  
            x = (x&d)+((x >> 2)&d);  
            x = (x&c)+((x >> 4)&c);  
            x = (x&b)+((x >> 8)&b);  
            x = (x&a)+((x >> 16)&a);  
            return x;  
              
        x = a ^ b  
        return x32(x >> 32) + x32(x)  

image = cv2.imread('datas/images/f1.jpg')
phascode = cal_phashcode(image)
phascode2 = cal_phashcode2(image)
print(phascode,phascode2)

# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print('cannot open camera')
#     exit(0)
# cv2.namedWindow("camera")
# cv2.setMouseCallback("camera",mouse_handler)

# while not gotBB:
#     ret,frame = cap.read()
#     if not ret:
#         print('read camera frame failed')
#         continue
#     cv2.imshow('camera',frame)
#     print('please select')
#     key = cv2.waitKey(10)
#     if key == 27:
#         break

# # cv2.setMouseCallback("camera",None)
# cv2.imshow('selected',frame[min(cur_x,rect_x):rect_width,min(cur_y,rect_y):rect_height])

# cv2.waitKey()
# cv2.destroyAllWindows()


    
    