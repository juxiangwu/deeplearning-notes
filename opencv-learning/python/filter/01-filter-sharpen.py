# -*- coding: utf-8 -*-

import cv2
import numpy as np
import os
cur_dir = os.getcwd()
print(cur_dir)
image_path = os.path.realpath(os.path.join(cur_dir,'opencv-learning/datas/f1.png'))
print(image_path)
def sharpen(img,dst):
    kernel = np.array([
            [-1, -1, -1],
            [-1, 9, -1],
            [-1, -1, -1]
            ])
    cv2.filter2D(img, -1, kernel, dst)
    
img = cv2.imread(image_path)
dst = img.copy()

sharpen(img, dst)

cv2.imshow("SRC", img)
cv2.imshow("DST", dst)

cv2.waitKey()
cv2.destroyAllWindows()