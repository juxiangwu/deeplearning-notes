# -*- coding:utf-8 -*-

'''
???????
'''

import cv2

hc = cv2.CascadeClassifier("temp/cvdata/haarcascades/haarcascade_frontalface_alt.xml")

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("cannot open camear")
    exit(0)

while True:
    ret,frame = camera.read()
    if not ret:
        continue
    cv2.imshow("Camera",frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()