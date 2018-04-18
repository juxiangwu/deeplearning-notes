#coding:utf-8

'''
马赛克效果
http://www.jb51.net/article/133431.htm
'''
import cv2
import numpy as np

point_lft = {'x':0,'y':0}
point_rgt = {'x':0,'y':0}
rows = 0
cols = 0
neightbourHood = 9
selected_x,selected_y = {},{}
selected = False
def mouse_handler(event,x,y,flat,params):
    global point_lft,point_rgt,rows,cols

    if event == cv2.EVENT_LBUTTONDOWN:
        point_lft['x'] = x
        point_lft['y'] = y

    elif event == cv2.EVENT_LBUTTONUP:

        if x > cols - 2 * neightbourHood:
            x = cols - 2 * neightbourHood
        
        if y > rows - 2 * neightbourHood:
            y = rows - 2 * neightbourHood

        point_rgt['x'] = x
        point_rgt['y'] = y

        selected_y = np.abs(point_rgt['y'] - point_lft['y'])
        selected_x = np.abs(point_rgt['x' - point_lft['x']])
        selected = True
        # for i in range(selected_y):
        #     for j in range(selected_x):
        #         rnd_num = np.random.randint(int(-neightbourHood / 2),int(neightbourHood /2 ))
        #         rect = {}
        #         rect['x'] = j + neightbourHood + point_lft['x']
        #         rect['y'] = i + neightbourHood + point_lft['y']
        #         rect['width'] = neightbourHood
        #         rect['height'] = neightbourHood

                
        
