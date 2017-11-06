# -*- coding: utf-8 -*-

import cv2
import numpy as np

def find_edge(img,dst):
    kernel = np.array([
            [-1,-1,-1],
            [-1, 8,-1],
            [-1,-1,-1]
            ])
    cv2.filter2D(img,-1,kernel,dst)
    
img = cv2.imread('../datas/f1.png')
dst = img.copy()

find_edge(img,dst)

cv2.imshow("SRC",img)
cv2.imshow("DST",dst)

cv2.waitKey()
cv2.destroyAllWindows()