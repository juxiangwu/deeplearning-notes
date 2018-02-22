# coding:utf-8
'''
绘制脸部轮廓
'''
# coding:utf-8
'''
脸部68个特征点检测
'''
import sys
import dlib
from skimage import io
import cv2
import numpy as np

# 加载并初始化检测器
# 模型下载地址http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('temp/dlib/shape_predictor_68_face_landmarks.dat')

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("cannot open camear")
    exit(0)

while True:
    ret,frame = camera.read()
    
    if not ret:
        continue
    frame_new = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    # 检测脸部
    dets = detector(frame_new, 1)
    print("Number of faces detected: {}".format(len(dets)))
    # 查找脸部位置
    for i, face in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {} ".format(
            i, face.left(), face.top(), face.right(), face.bottom()))
        # 绘制脸部位置
        cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 1)
        shape = predictor(frame_new, face)
        # print(shape.part(0),shape.part(1))
        # 绘制特征点
        points = []
        for i in range(68):
            cv2.circle(frame,(shape.part(i).x,shape.part(i).y),3,(0,0,255),2)
            cv2.putText(frame,str(i),(shape.part(i).x,shape.part(i).y),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),1)
            points.append([shape.part(i).x,shape.part(i).y])
    cv2.imshow("Camera",frame)
    frame_pose = cv2.cvtColor(frame_new,cv2.COLOR_RGB2BGR)
    # cv2.polylines(frame_pose,[np.array(points,np.int32)],False,(0,255,0),1)
    cv2.imshow('Face-Pose',frame_pose)
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
