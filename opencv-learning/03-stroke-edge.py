# -*- coding: utf-8 -*-
import cv2

def strokeEdge(src,dst,blurKsize=7,edgeKsize = 5):
    if blurKsize >= 3:
        blurredSrc = cv2.medianBlur(src,blurKsize)
        graySrc = cv2.cvtColor(blurredSrc,cv2.COLOR_BGR2GRAY)
    else:
        graySrc = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
    
    cv2.Laplacian(graySrc,cv2.CV_8U,graySrc,ksize = edgeKsize)
    normalizedInversedAlpha = (1.0 / 255) * (255 - graySrc)
    channels = cv2.split(src)
    for channel in channels:
        channel[:] = channel * normalizedInversedAlpha
    cv2.merge(channels,dst)
    

img = cv2.imread('datas/img1.jpg')
dst = img.copy()

strokeEdge(img,dst)

cv2.imshow("Edge-SRC",img)
cv2.imshow("Edge",dst)

cv2.waitKey()
cv2.destroyAllWindows()
