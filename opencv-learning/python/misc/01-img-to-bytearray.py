# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np
import os

rdmarray = bytearray(os.urandom(120000))
flatarray = np.array(rdmarray)

grayImg = flatarray.reshape(300,400)
bgrImg = flatarray.reshape(100,400,3)

cv.imshow("gray",grayImg)
cv.imshow("rgb",bgrImg)

cv.waitKey()