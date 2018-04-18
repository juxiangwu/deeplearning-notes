#coding:utf-8
'''
图像旋转
'''

import numpy as np
import cv2

def image_rotate(image,angle):

    alpha = angle * np.pi / 180.0

    # 旋转矩阵
    rotate_matrix = [
        [np.cos(alpha),-1 * np.sin(alpha),0],
        [np.sin(alpha), np.cos(alpha),0],
        [0,0,1]
        ]

    rows = image.shape[0]
    cols = image.shape[1]

    # 图像旋转后顶点计算
    a1 = cols * rotate_matrix[0][0]
    b1 = cols * rotate_matrix[1][0]

    a2 = cols * rotate_matrix[0][1] + rows * rotate_matrix[0][1]
    b2 = cols * rotate_matrix[1][0] + rows * rotate_matrix[1][1]

    a3 = rows * rotate_matrix[0][1]
    b3 = rows * rotate_matrix[1][1]

    # 计算极值点

    x_min = min(min(min(0.0,a1),a2),a3)
    x_max = max(max(max(0.0,a1),a2),a3)

    y_min = min(min(min(0.0,b1),b2),b3)
    y_max = max(max(max(0.0,b1),b2),b3)

    out_rows = int(np.abs(x_max - x_min))
    out_cols = int(np.abs(y_max - y_min))
    print('src size:(%d,%d)' %(rows,cols))
    print('new size:(%d,%d)' % (out_rows,out_cols))
    dist = np.zeros((out_rows,out_cols,image.shape[2]),image.dtype)
    for i in range(out_rows):
        for j in range(out_cols):
            x = int((j + x_min) * rotate_matrix[0][0]  - (i + y_min) * rotate_matrix[0][1])
            y = int(-1 * (j + x_min) * rotate_matrix[1][0] + (i + y_min) * rotate_matrix[1][1])
            
            if x >= 0 and y >= 0 and x < rows and y < cols:
                # print('i = %d,j = %d;x = %d,y = %d' % (i,j,x,y))
                dist[i,j] = image[x,y]

    return dist


image = cv2.imread('datas/l1.jpg')
result = image_rotate(image,45)

cv2.imshow('src',image)
cv2.imshow('rotate:60',cv2.resize(result,(int(result.shape[0] / 2),int(result.shape[1] / 2))))

cv2.waitKey()
cv2.destroyAllWindows()



