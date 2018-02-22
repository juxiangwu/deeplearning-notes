#coding:utf-8
'''
脸部识别
'''
import sys
import dlib
from skimage import io
import cv2

# 加载并初始化检测器
# 模型下载地址http://dlib.net/files/mmod_human_face_detector.dat.bz2
cnn_face_detector = dlib.cnn_face_detection_model_v1('temp/dlib/mmod_human_face_detector.dat')

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
    dets = cnn_face_detector(frame_new, 1)
    print("Number of faces detected: {}".format(len(dets)))
    # 查找脸部位置
    for i, face in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {} Confidence: {}".format(
            i, face.rect.left(), face.rect.top(), face.rect.right(), face.rect.bottom(), face.confidence))
        # 绘制脸部位置
        cv2.rectangle(frame, (face.rect.left(), face.rect.top()), (face.rect.right(), face.rect.bottom()), (0, 255, 0), 3)
    cv2.imshow("Camera",frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
