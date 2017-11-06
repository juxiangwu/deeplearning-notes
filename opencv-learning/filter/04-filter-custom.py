# -*- coding: utf-8 -*-

import cv2
import numpy as np

def sharpen(img,dst):
    kernel = np.array([
            [-2,-1, 0],
            [-1, 1, 1],
            [ 0, 1, 2]
            ])
    cv2.filter2D(img,-1,kernel,dst)
    
img = cv2.imread('../datas/f1.png')
dst = img.copy()

sharpen(img,dst)

cv2.imshow("SRC",img)
cv2.imshow("DST",dst)

cv2.waitKey()
cv2.destroyAllWindows()