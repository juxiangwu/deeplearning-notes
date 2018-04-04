# -*- coding:utf-8 -*-

import cv2
import numpy as np
detector = cv2.SimpleBlobDetector.create()
#keypoints = []

img = cv2.imread("temp/screen.png",cv2.IMREAD_GRAYSCALE)

keypoints = detector.detect(img)

imout = cv2.drawKeypoints(img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("IMG",img)
cv2.imshow("OUT",imout)

cv2.waitKey()