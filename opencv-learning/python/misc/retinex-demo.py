# -*- coding: utf-8 -*-

import cv2
import numpy as np

def enhance_channel(channel):
    res = channel / np.max(channel)
    imretinex = np.round(np.exp(res * 5.54))
    
    out = np.uint8(imretinex)
    
    return out

def retinex_add(img):
    w,h,c = img.shape;
    imgout = np.zeros(img.shape,np.uint8)
    channels = cv2.split(img)
    for i in range(c):
        imchannel = np.double(channels[i]) + 2.2204e-016
        imgout[:,:,i] = enhance_channel(imchannel)
    #res = cv2.merge(imgout)
   # print(res.shape)
    #out = np.max(np.min(res[:]),0)
    return imgout

def singleScaleRetinex(img, sigma):

    retinex = np.log10(img) - np.log10(cv2.GaussianBlur(img, (0, 0), sigma))

    return retinex

def multiScaleRetinex(img, sigma_list=[15, 80, 250]):

    retinex = np.zeros_like(img,np.float16)
    for sigma in sigma_list:
        retinex += singleScaleRetinex(img, sigma)

    retinex = retinex / len(sigma_list)

    return retinex



img = cv2.imread('../datas/d1.png')


cv2.imshow("img",img)

res = multiScaleRetinex(img)

cv2.imshow("dst",np.uint8(res))
cv2.waitKey()
cv2.destroyAllWindows()