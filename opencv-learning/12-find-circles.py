# -*- coding: utf-8 -*-
import cv2
import numpy as np

img = cv2.imread('datas/b2.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray,5)

circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,120,
                           param1=100,param2=30,minRadius=0,
                           maxRadius=0)

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    cv2.circle(img,(i[0],i[1]),2,(0,255,0),2)
    

cv2.imshow("IMG",img)
cv2.waitKey()
cv2.destroyAllWindows()
