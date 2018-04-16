#coding:utf-8
'''
基于哈希算法的物体跟踪
'''
import cv2  
import numpy as np  
import time  
from glob import iglob  
  
  
class HashTracker:  
    def __init__(self, frame):  
        # 初始化图像  
        self.img = frame
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)  
  
    def cal_hash_code(self, cur_gray):  
        s_img = cv2.resize(cur_gray, dsize=(8, 8))  
        img_mean = cv2.mean(s_img)  
        return s_img > img_mean[0]  
  
    def cal_phash_code(self, cur_gray):  
        # 缩小至32*32  
        m_img = cv2.resize(cur_gray, dsize=(32, 32))  
        # 浮点型用于计算  
        m_img = np.float32(m_img)  
        # 离散余弦变换，得到dct系数矩阵  
        img_dct = cv2.dct(m_img)  
        img_mean = cv2.mean(img_dct[0:8, 0:8])  
        # 返回一个8*8bool矩阵  
        return img_dct[0:8, 0:8] > img_mean[0]  
  
    def cal_dhash_code(self, cur_gray):  
        # dsize=(width, height)  
        m_img = cv2.resize(cur_gray, dsize=(9, 8))  
        m_img = np.int8(m_img)  
        # 得到8*8差值矩阵  
        m_img_diff = m_img[:, :-1] - m_img[:, 1:]  
        return m_img_diff > 0  
  
    def cal_hamming_distance(self, model_hash_code, search_hash_code):  
        # 返回不相同的个数  
        diff = np.uint8(np.bitwise_xor(model_hash_code,search_hash_code))
        return cv2.countNonZero(diff)  
  
    def hash_track(self, roi, rect, flag=0):  
        # 获得矩形框信息  
        width = abs(rect[0] - rect[2])  
        height = abs(rect[1] - rect[3])  
        # 获得当前图像的长宽信息  
        img_w, img_h = self.img.shape[:2]  
        # 根据flag，选择方法，计算前一帧的hash值  
        if flag == 0:  
            model_hash_code = self.cal_hash_code(roi)  
        elif flag == 1:  
            model_hash_code = self.cal_phash_code(roi)  
        elif flag == 2:  
            model_hash_code = self.cal_dhash_code(roi)  
        # 初始化汉明距离  
        min_dis = 64  
        # 滑动窗口匹配,步长为2  
        for i in range(0, img_h, 2):  
            for j in range(0, img_w, 2):  
                if flag == 0:  
                    search_hash_code = self.cal_hash_code(self.gray[j:j + height, i:i + width])  
                elif flag == 1:  
                    search_hash_code = self.cal_phash_code(self.gray[j:j + height, i:i + width])  
                elif flag == 2:  
                    search_hash_code = self.cal_dhash_code(self.gray[j:j + height, i:i + width])  
                # 计算汉明距离  
                distance = self.cal_hamming_distance(model_hash_code, search_hash_code)  
                # 获得最小汉明距离，同时得到此时的匹配框  
                if distance < min_dis:  
                    rect = i, j, i + width, j + height  
                    min_dis = distance  
        # 根据匹配框，获得下一帧的匹配模板  
        roi = self.gray[rect[1]:rect[3], rect[0]:rect[2]]  
        # 显示当前帧矩形框位置  
        cv2.rectangle(self.img, (rect[0], rect[1]), (rect[2], rect[3]), (255, 0, 0), 2)  
        return roi  
  
  
# 鼠标响应函数  
box = [0]*4  
gotBB = False
  
def mouse_handler(event, x, y, flag, param):
    global gotBB
    if gotBB:
        return
    if event == cv2.EVENT_LBUTTONDOWN:  
        # 起始点记录  
        box[0], box[1] = x, y  
    elif event == cv2.EVENT_MOUSEMOVE and flag == cv2.EVENT_FLAG_LBUTTON:  
        box[2], box[3] = x, y  
    elif event == cv2.EVENT_LBUTTONUP:  
        # 获得右下角点  
        box[2], box[3] = x, y
        gotBB = True
  
  
def main():  
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print('cannot open camera')
        exit(0)
    cv2.namedWindow('camera')
    cv2.setMouseCallback('camera', mouse_handler)
    model = None
    gray = None
    while True:
        ret,frame = cap.read()
        if not ret:
            print('cannot grab frame from camera')
            continue
        while not gotBB:
            ret,frame = cap.read()
            if not ret:
                print('cannot grab frame from camera')
                continue
            cv2.imshow('camera',frame)
            key = cv2.waitKey(10)
            gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)

        # cv2.setMouseCallback('camera', None)
        model = gray[box[1]:box[3], box[0]:box[2]]
        ht = HashTracker(frame)
        model = ht.hash_track(model,box)
        cv2.imshow('camera',frame)

        key = cv2.waitKey(10)
        if key == 27:
            break
    cv2.destroyAllWindows()

    # # 读取第一张图片，用来画框  
    # img = cv2.imread('./img/0001.jpg')  
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    # cv2.namedWindow('hashTracker', 1)  
    # cv2.setMouseCallback('hashTracker', mouse_handler)  
    # while True:  
    #     cv2.imshow('hashTracker', img)  
    #     if cv2.waitKey(1) == 27:  
    #         break  
    # # 获取初始化模型  
    # model = gray[box[1]:box[3], box[0]:box[2]]  
    # # 获取图片序列  
    # paths = iglob(r'./img/*.jpg')  
    # # 计数用  
    # frame_count = 0  
    # # 循环读入图片  
    # for path in paths:  
    #     frame_count += 1  
    #     # 实例创建  
    #     h = HashTracker(path)  
    #     # 感知哈希跟踪  
    #     start_time = time.clock()  
    #     model = h.hash_track(model, box)  
    #     fin_time = time.clock()  
  
    #     print "%d: delta time:%.2f" % (frame_count, fin_time - start_time)  
    #     cv2.imshow('hashTracker', h.img)  
    #     if cv2.waitKey(20) == 27:  
    #         break  
  
  
if __name__ == '__main__':  
    main()  