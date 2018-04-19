#coding:utf-8
'''
二值图像的腐蚀运算
定义：
    g(x,y) = erode[f(x,y),B] = AND[Bf(x,y)]
    其中，g(x,y)为腐蚀后的二值图像，f(x,y)为原始二值图像
    B为结构元素，Bf(x,y)定义为
    Bf(x,y) = {f(x - bx,y-by),(bx,by)∈B}
    算子AND(x(i),...,x(n))定义为：当且仅当x(1) = ... = x(n) = 1时，
    AND(x(1),...,x(n))等于1，否则为0

结构元素选择的原则往往是具有旋转不变性，或者镜像不变性。也就是说，结构元素
原点在其几何中心处理，并且其他像素关于该原点对你。常用到的结构元素：
1、水平单列；2、垂直单列；3、十字形；4、方形
'''
import cv2
import numpy as np
# 3位水平方向结构元素
def erode_horizontal_3x1(image):
    img_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    rows,cols = img_gray.shape
    gray_flat = img_gray.reshape((rows * cols,))
    # 创建空白图像
    dist = np.full(img_gray.shape,fill_value=255,dtype=img_gray.dtype).reshape((rows * cols,))
    x_coord = np.arange(1,cols-1)
    for i in range(rows):
        for j in x_coord:
            mid = gray_flat[i * cols + j]
            lft = gray_flat[i * cols + j + 1]
            rgt = gray_flat[i * cols + j - 1]
            if mid == 0 and lft == 0 and rgt == 0:
                dist[i * cols + j] = 0
    return dist.reshape((rows,cols))

# 5位水平方向结构元素
def erode_horizontal_5x1(image):
    img_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    rows,cols = img_gray.shape
    gray_flat = img_gray.reshape((rows * cols,))
    # 创建空白图像
    dist = np.full(img_gray.shape,fill_value=255,dtype=img_gray.dtype).reshape((rows * cols,))
    x_coord = np.arange(2,cols-2)
    for i in range(rows):
        for j in x_coord:
            lft2 = gray_flat[i * cols + j -2]
            rgt = gray_flat[i * cols + j - 1]
            mid = gray_flat[i * cols + j]
            lft = gray_flat[i * cols + j + 1]
            rgt2 = gray_flat[i * cols + j + 2]
            if mid == 0 and lft == 0 and rgt == 0 and lft2 == 0 and rgt2 == 0:
                dist[i * cols + j] = 0
    return dist.reshape((rows,cols))

# 3位垂直方向结构元素
def erode_vertical_3x1(image):
    img_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    rows,cols = img_gray.shape
    gray_flat = img_gray.reshape((rows * cols,))
    # 创建空白图像
    dist = np.full(img_gray.shape,fill_value=255,dtype=img_gray.dtype).reshape((rows * cols,))
    y_coord = np.arange(1,rows-1)
    for i in y_coord:
        for j in range(cols):
            mid = gray_flat[i * cols + j]
            lft = gray_flat[(i + 1) * cols + j]
            rgt = gray_flat[(i - 1) * cols + j]
            if mid == 0 and lft == 0 and rgt == 0:
                dist[i * cols + j] = 0
    return dist.reshape((rows,cols))

# 5位垂直方向结构元素
def erode_vertical_5x1(image):
    img_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    rows,cols = img_gray.shape
    gray_flat = img_gray.reshape((rows * cols,))
    # 创建空白图像
    dist = np.full(img_gray.shape,fill_value=255,dtype=img_gray.dtype).reshape((rows * cols,))
    y_coord = np.arange(2,rows - 2)
    for i in y_coord:
        for j in range(cols):
            lft2 = gray_flat[(i - 2) * cols + j]
            rgt = gray_flat[(i - 1) * cols + j]
            mid = gray_flat[i * cols + j]
            lft = gray_flat[(i + 1) * cols + j]
            rgt2 = gray_flat[(i + 2) * cols + j]
            if mid == 0 and lft == 0 and rgt == 0 and lft2 == 0 and rgt2 == 0:
                dist[i * cols + j] = 0
    return dist.reshape((rows,cols))

# 3位方形结构元素
def erode_cross_3x3(image):
    img_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    rows,cols = img_gray.shape
    gray_flat = img_gray.reshape((rows * cols,))
    # 创建空白图像
    dist = np.full(img_gray.shape,fill_value=255,dtype=img_gray.dtype).reshape((rows * cols,))
    y_coord = np.arange(1,rows - 1)
    x_coord = np.arange(1,cols - 1)

    for i in y_coord:
        for j in x_coord:
            p1 = gray_flat[i * cols + j]
            p2 = gray_flat[(i - 1) * cols + j]
            p3 = gray_flat[(i + 1) * cols + j]

            p4 = gray_flat[i * cols + (j - 1)]
            p5 = gray_flat[(i - 1) * cols + (j - 1)]
            p6 = gray_flat[(i + 1) * cols + (j - 1)]

            p7 = gray_flat[(i - 1) * cols + (j + 1)]
            p8 = gray_flat[i * cols + (j + 1)]
            p9 = gray_flat[(i + 1) * cols + (j + 1)]

            if p1 == 0 and p2 == 0 and p3 == 0 and \
                p4 == 0 and p5 == 0 and p6 == 0 and \
                p7 == 0 and p8 == 0 and p9 == 0:

                dist[i * cols + j] = 0

    return dist.reshape((rows,cols))


src = cv2.imread('datas/b.png')
dist_h3x1 = erode_horizontal_3x1(src)
dist_h5x1 = erode_horizontal_5x1(src)
dist_v3x1 = erode_vertical_3x1(src)
dist_v5x1 = erode_vertical_5x1(src)
dist_c3x3 = erode_cross_3x3(src)

cv2.imshow('src',src)
cv2.imshow('horizontal-3x1',dist_h3x1)
cv2.imshow('horizontal-5x1',dist_h5x1)
cv2.imshow('vertical-3x1',dist_v3x1)
cv2.imshow('vertical-5x1',dist_v5x1)
cv2.imshow('cross-3x3',dist_c3x3)

cv2.waitKey()
cv2.destroyAllWindows()