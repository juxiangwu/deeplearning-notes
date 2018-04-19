#coding:utf-8

'''
马赛克效果
'''
import cv2
import numpy as np

point_start = {'x':0,'y':0}
point_end = {'x':0,'y':0}
rows = 0
cols = 0

selected = False

def mosaic(selected_image,nsize=9):
    rows,cols,_ = selected_image.shape
    dist = selected_image.copy()
    # 划分小方块，每个小方块填充随机颜色
    for y in range(0,rows,nsize):
        for x in range(0,cols,nsize):
            dist[y:y+nsize,x:x+nsize] = (np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255))
    return dist

def mouse_handler(event,x,y,flag,params):
    global point_lft,point_rgt,selected
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print('button down')
        point_start['x'] = x
        point_start['y'] = y

    if event == cv2.EVENT_LBUTTONUP:
        print('button up')
        point_end['x'] = x
        point_end['y'] = y
        selected = True
    
src = cv2.imread('datas/images/f2.jpg')
rows,cols,_ = src.shape
src_cpy = src.copy()
cv2.namedWindow("src")
cv2.setMouseCallback("src",mouse_handler)

while not selected:
    cv2.imshow('src',src)
    key = cv2.waitKey(10)

# 处理选择的矩形
rect = {}
if point_start['x'] < point_end['x']:
    rect['x'] = point_start['x']
    rect['y'] = point_start['y']
    rect['width'] = np.abs(point_end['x'] - point_start['x'])
    rect['height'] = np.abs(point_end['y'] - point_start['y'])
    cv2.rectangle(src,(point_start['x'],point_start['y']),(point_end['x'],point_end['y']),(255,0,0),3)
else:
    rect['x'] = point_end['x']
    rect['y'] = point_end['y']
    rect['width'] = np.abs(point_end['x'] - point_start['x'])
    rect['height'] = np.abs(point_end['y'] - point_start['y'])
    cv2.rectangle(src,(point_end['x'],point_end['y']),(point_start['x'],point_start['y']),(255,0,0),3)

cv2.imshow('src',src)
print('selected rect = ',rect)
# 选择图像
select_image = src_cpy[rect['y']:rect['y']+rect['height'],
                    rect['x']:rect['x']+rect['height']]
result = mosaic(select_image)
# 将处理完成的区域合并回原图像
src_cpy[rect['y']:rect['y']+rect['height'],
        rect['x']:rect['x']+rect['height']] = cv2.addWeighted(result,0.65,select_image,0.35,2.0)
cv2.imshow('result',src_cpy)
cv2.waitKey()
cv2.destroyAllWindows()

        
