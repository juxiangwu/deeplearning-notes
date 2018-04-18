#coding:utf-8
'''
图像缩放
'''
import numpy as np
import cv2

image = cv2.imread('datas/l1.jpg')

# 基于等隔提取图像缩放
def scale_simple(image,kx,ky):
    # 计算缩放后图像的分辨率
    rows = int(np.round(np.abs(image.shape[0] * kx)))
    cols = int(np.round(np.abs(image.shape[1] * ky)))
    
    dist = None

    if len(image.shape) == 3 and image.shape[2] >= 3:
        dist = np.zeros((rows,cols,image.shape[2]),image.dtype)
    else:
        dist = np.zeros((rows,cols),image.dtype)

    for y in range(rows):
        for x in range(cols):

            new_y =  int((y + 1) / ky + 0.5) - 1
            new_x = int((x + 1) / kx + 0.5) - 1

            dist[y,x] = image[new_y,new_x]

    return dist

# 基于区域子块提取图像缩放
def area_average(image,left_point,right_point):
    temp1,temp2,temp3 = 0,0,0
    # 计算区域子块像素点个数
    #npix = (right_point['x'] - left_point['x'] + 1) * (right_point['y'] - left_point['y'] + 1)

    # 对区域子块各个通道对像素值求和

    for i in range(right_point['x'] - left_point['x']):
        i += left_point['x']
        for j in range(right_point['y'] - left_point['y']):
            
            j += right_point['y']

            temp1 += image[i,j,0]
            temp2 += image[i,j,1]
            temp3 += image[i,j,2]

    vec3b = [temp1,temp2,temp3]

    return vec3b

def scale_area(image, kx,ky):
    rows = int(np.round(np.abs(image.shape[0] * kx)))
    cols = int(np.round(np.abs(image.shape[1] * ky)))

    dist = np.zeros((rows,cols,image.shape[2]),image.dtype)

    left_row_coord = 0
    left_col_coord = 0

    for i in range(rows):
        x = int((i + 1) / kx + 0.5) - 1
        for j in range(cols):
            y = int((j + 1) / ky + 0.5) - 1
            left_point = {'x':left_row_coord,'y':left_col_coord}
            right_point = {'x':x,'y':y}
            pixel = area_average(image,left_point,right_point)
            dist[i,j] = pixel

            left_col_coord = y + 1
    
        left_col_coord = 0
        left_row_coord = x + 1
    
    return dist
result = scale_simple(image,0.5,0.5)
result2 = scale_area(image,0.5,0.5)
cv2.imshow('src',image)
cv2.imshow('scale-simple',result)
cv2.imshow('scale-area',result2)

cv2.waitKey()
cv2.destroyAllWindows()