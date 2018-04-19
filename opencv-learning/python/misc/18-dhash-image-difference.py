#coding:utf-8
'''
基于dHash算法计算图像的相似度
'''

import numpy as np
import cv2

# 计算图像差值
def cal_image_difference(image):

    # 缩放图像大小9x8
    new_img = cv2.resize(image,(8,9))
    # 转化成灰度图像
    gray = cv2.cvtColor(new_img,cv2.COLOR_RGB2GRAY)
    rows,cols = gray.shape[0],gray.shape[1]
    # 比较相邻像素
    pixels = gray.reshape((8*9,)).tolist()
    # print('pixels = ',pixels)
    difference = []
    for y in range(rows):
        idx = y * cols
        for x in range(cols - 1):
            lft_pixel_idx = idx + x
            difference.append(pixels[lft_pixel_idx] > pixels[lft_pixel_idx + 1])
    return difference

# 计算两个哈希值的汉明距离
def cal_hash_hamming_distance(dhash1,dhash2):
    difference = (int(dhash1, 16)) ^ (int(dhash2, 16))
    return bin(difference).count("1")

# 比较两个图像的汉明距离
def cal_image_hamming_distance(image1,image2):
    hamming_distance = 0
    img_hdist1 = cal_image_difference(image1)
    img_hdist2 = cal_image_difference(image2)

    for index,img1_pix in enumerate(img_hdist1):
        img2_pix = img_hdist2[index]
        if img1_pix != img2_pix:
            hamming_distance += 1

    return hamming_distance

# 计算图像dHash值
def cal_image_dhash(image):
    difference = cal_image_difference(image)
    hash_str = ""
    decimal_val = 0

    for index,value in enumerate(difference):
        if value:
            decimal_val += value * (2 ** (index % 8))
        if index % 8 == 7: # 结束
            hash_str += str(hex(decimal_val)[2:].rjust(2, "0"))
            decimal_val = 0
    return hash_str

def cal_image_similar(image1,image2):
    img1_hash = cal_image_dhash(image1)
    img2_hash = cal_image_dhash(image2)
    difference = cal_hash_hamming_distance(img1_hash,img2_hash)
    return difference

# 如果汉明距离值小于5的话，基本可以认为是相同图片
image1 = cv2.imread('datas/l1.jpg')
image2 = cv2.imread('datas/l2.jpg')
image3 = cv2.imread('datas/l3.jpg')
image4 = cv2.imread('datas/p1.jpg')
image5 = cv2.imread('datas/p3.jpg')
diff1 = cal_image_similar(image1,image2)
print('diff1 = ',diff1)
diff2 = cal_image_similar(image1,image3)
print('diff2 = ',diff2)
diff3 = cal_image_similar(image1,image4)
print('diff3 = ',diff3)
diff4 = cal_image_similar(image4,image5)
print('diff4 = ',diff4)
