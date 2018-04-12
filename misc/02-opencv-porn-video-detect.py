#coding:utf-8
'''
OpenCV+nude.py实现视频黄色帧检测
'''
from nudecv import NudeCV
import cv2

cap = cv2.VideoCapture('datas/videos/orgasm-sex.mp4')

while (cap.isOpened()):
    ret,frame = cap.read()
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    n = NudeCV(cv2.resize(frame,(240,360)))
    n.parse()
    print("damita :", n.result, n.inspect())
    if n.result:
        cv2.imshow('NudeCV',cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
    cv2.imshow('Video',cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
    key = cv2.waitKey(10)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()