# -*- coding: utf-8 -*-
'''
检测边界
'''
import cv2
import numpy as np

img = cv2.imread('datas/b2.jpg',cv2.IMREAD_UNCHANGED)
img2 = cv2.pyrDown(img)
gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,125,255,cv2.THRESH_BINARY)

image,contours,hier = cv2.findContours(thresh,cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    ret = cv2.minAreaRect(c)
    box = cv2.boxPoints(ret)
    box = np.int0(box)
    cv2.drawContours(img,[box],0,(0,255,0),3)
    
    (x,y),radius = cv2.minEnclosingCircle(c)
    center = (int(x),int(y))
    radius = int(radius)
    
    img = cv2.circle(img,center,radius,(0,255,0),2)

cv2.drawContours(img,contours,-1,(255,0,0),2)
cv2.imshow("IMG",img)

cv2.waitKey()
cv2.destroyAllWindows()