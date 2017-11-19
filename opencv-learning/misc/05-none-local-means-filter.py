# -*- coding: utf-8 -*-
'''
非局部均值滤波算法
'''
import cv2
import numpy as np
def psnr(A, B):
    return 10*np.log(255*255.0/(((A.astype(np.float)-B)**2).mean()))/np.log(10)

def double2uint8(I, ratio=1.0):
    return np.clip(np.round(I*ratio), 0, 255).astype(np.uint8)

def make_kernel(f):
    f = int(f)
    kernel = np.zeros((int(2*f+1), int(2*f+1)))
    for d in range(1, int(f+1)):
        kernel[f-d:f+d+1, f-d:f+d+1] += (1.0/((2*d+1)**2))
    return kernel/kernel.sum()

def NLmeansfilter(I, h_=10, templateWindowSize=5,  searchWindowSize=11):
    f = int(templateWindowSize/2)
    t = int(searchWindowSize/2)
    height, width = I.shape[:2]
    padLength = t+f
    I2 = np.pad(I, int(padLength), 'symmetric')
    kernel = make_kernel(f)
    h = (h_**2)
    I_ = I2[padLength-f:padLength+f+height, padLength-f:padLength+f+width]

    average = np.zeros(I.shape)
    sweight = np.zeros(I.shape)
    wmax =  np.zeros(I.shape)
    for i in range(-t, t+1):
        for j in range(-t, t+1):
            if i==0 and j==0:
                continue
            I2_ = I2[padLength+i-f:padLength+i+f+height, padLength+j-f:padLength+j+f+width]
            w = np.exp(-cv2.filter2D((I2_ - I_)**2, -1, kernel)/h)[f:f+height, f:f+width]
            sweight += w
            wmax = np.maximum(wmax, w)
            average += (w*I2_[f:f+height, f:f+width])
    return (average+wmax*I)/(sweight+wmax)

if __name__ == '__main__':
    I = cv2.imread('../datas/f1.png', 0)

    sigma = 20.0
    I1 = double2uint8(I + np.random.randn(*I.shape) *sigma)
    print ('Noise:PSNR',psnr(I, I1))
    R1  = cv2.medianBlur(I1, 5)
    print ('median filter:PSNR',psnr(I, R1))
    R2 = cv2.fastNlMeansDenoising(I1, None, sigma, 5, 11)
    print ('OpenCV NLM:',psnr(I, R2))
    R3 = double2uint8(NLmeansfilter(I1.astype(np.float), sigma, 5, 11))
    print ('NLM PSNR',psnr(I, R3))