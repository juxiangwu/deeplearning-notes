# -*- coding: utf-8 -*-
import cv2,wx
import numpy as np
from readHdr import readHdr             #readHdr程序代码参见下一遍博客
 
def zmMinFilterGray(src, r=7):          #计算最小值滤波，r是滤波器半径
    '''if r <= 0:
        return src
    h, w = src.shape[:2]
    I = src
    res = np.minimum(I  , I[[0]+range(h-1)  , :])
    res = np.minimum(res, I[range(1,h)+[h-1], :])
    I = res
    res = np.minimum(I  , I[:, [0]+range(w-1)])
    res = np.minimum(res, I[:, range(1,w)+[w-1]])
    return zmMinFilterGray(res, r-1)'''
    return cv2.erode(src, np.ones((2*r+1, 2*r+1)))
 
def guidedfilter(I, p, r, eps):         #引导滤波
    height, width = I.shape
    m_I = cv2.boxFilter(I, -1, (r,r))
    m_p = cv2.boxFilter(p, -1, (r,r))
    m_Ip = cv2.boxFilter(I*p, -1, (r,r))
    cov_Ip = m_Ip-m_I*m_p
 
    m_II = cv2.boxFilter(I*I, -1, (r,r))
    var_I = m_II-m_I*m_I
 
    a = cov_Ip/(var_I+eps)
    b = m_p-a*m_I
 
    m_a = cv2.boxFilter(a, -1, (r,r))
    m_b = cv2.boxFilter(b, -1, (r,r))
    return m_a*I+m_b
 
def stretchImage2(data, vv = 10.0):        #非线性拉伸
    m = data-data.mean()
    S = np.sign(m)
    A = np.abs(m)
    A = 1.0 - vv**(-A)
    m = S*A
    vmin, vmax = m.min(), m.max()
    return (m-vmin)/(vmax-vmin)
 
def getV1(m, r, eps, ratio):     #对所有通道求同样暗边界
    tmp = np.min(m,2)
    V1 = cv2.blur(zmMinFilterGray(tmp, 7), (7,7))
    V1 = guidedfilter(tmp, V1, r, eps)
    V1 = np.minimum(V1, tmp)
    V1 = np.minimum(V1*ratio, 1.0)
    return V1
 
def getV2(m, r, eps, ratio):
    Y = np.zeros(m.shape)
    for k in range(3):                         #对每个通道单独求亮边界
        v2 = 1 - cv2.blur(zmMinFilterGray(1-m[:,:,k],7), (7,7))
        v2 = guidedfilter(m[:,:,k], v2, r, eps)
        v2 = np.maximum(v2, m[:,:,k])
        Y[:,:,k] = np.maximum(1-(1-v2)*ratio, 0.0)
    return Y
 
def ProcessHdr(m, r, eps, ratio, para1):                                 #单尺度处理
    V1 = getV1(m, r, eps, ratio)                #计算暗边界
    V2 = getV2(m, r, eps, ratio)                #计算亮边界
    Y = np.zeros(m.shape)
    for k in range(3):
        Y[:,:,k] = ((m[:,:,k]-V1)/(V2[:,:,k]-V1))
    Y = stretchImage2(Y,para1)                  #非线性拉伸
    return Y
 
 
def ProcessHdrMs(m, r=[161], eps=[0.005,0.001, 0.01], ratio=[0.98, 0.98, 0.92], para1=10.0):    #多尺度处理
    Y = []
    for k in range(len(r)):
        Y.append(ProcessHdr(m, r[k], eps[k], ratio[k], para1))
 
    return sum(Y)/len(r)
 
if __name__ == '__main__':
    import glob,os.path
    for d in ['auto.hdr',]:                               
        m = readHdr(d)                                              #读取dhr文件， readHdr程序代码参见下一遍博客
        m1,m2 = m.max(), m.min()
        m = (m-m2)/(m1-m2) *255                                     #数据拉伸到[0,255]
        m1 = m[:,:,0].copy();  m[:,:,0] = m[:,:,2]; m[:,:,2]=m1     #颜色通道调整，opencv里R和B反了
 
        m = np.log(m+1)/np.log(256)                                 #log处理
        for i in range(2):                                          #如果图像还是很暗，则需要多次log处理
            tmp = np.max(m,2)
            tmp = guidedfilter(tmp, tmp, 301, 0.01)
            th = np.mean(tmp<0.05)
            if th < 0.3:
                break
            m1 = np.log(m*255+1)/np.log(256)
            tmp = np.clip(tmp, 0.0, 1.0) ** (0.05)                  #tmp是权重参数
            for k in range(3):                                      #取加权平均
                m[:,:,k] = tmp*m[:,:,k] + (1-tmp)*m1[:,:,k]
                 
        m2 = ProcessHdrMs(m)*255
        cv2.imwrite('%s.jpg' % d.split('.')[0], m2)
