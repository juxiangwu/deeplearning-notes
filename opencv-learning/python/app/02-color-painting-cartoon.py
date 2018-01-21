# -*- coding: utf-8 -*-

import cv2

img = cv2.imread('../datas/f1.png')
cols,rows,channel = img.shape;

#smallImg = cv2.resize(img,(int(cols / 2),int(rows / 2)),interpolation=cv2.INTER_CUBIC)

cv2.imshow("SRC",img)
#cv2.imshow("S_SRC",smallImg)
#temp = img.copy()
#dst = img.copy()
#for i in range(7):
#    blur = cv2.bilateralFilter(img,9,9,7)    
#    dst = cv2.bilateralFilter(blur,9,9,7) 
    #dst = cv2.bilateralFilter(tmp,9,9,7)
#dst.setTo(0)
#img.copyTo(dst)
#cv2.imshow("DST",dst)

cv2.waitKey()
cv2.destroyAllWindows()
