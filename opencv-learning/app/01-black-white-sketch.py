# -*- coding: utf-8 -*-
import cv2

img = cv2.imread('../datas/f1.png')

gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

BLUR_SIZE = 7
blur = cv2.medianBlur(gray,BLUR_SIZE)
LP_FILTER_SIZE = 5

edges = cv2.Laplacian(blur,cv2.CV_8UC1,LP_FILTER_SIZE)
#mask = gray.copy()
_,mask = cv2.threshold(edges,8,255,cv2.THRESH_BINARY_INV)

cv2.imshow("SRC",img)
cv2.imshow("DST",mask)

cv2.waitKey()
cv2.destroyAllWindows()