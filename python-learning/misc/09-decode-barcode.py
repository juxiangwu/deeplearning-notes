#coding:utf-8
'''
通过摄像头识别一维条形码
'''

import cv2
from pyzbar.pyzbar import decode

# results = decode(cv2.imread('datas/images/barcode-3.jpg'))
# for result in results:
#     print('barcode = %s'% str(result.data))

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('cannot open camera 0')
    exit(0)

while True:
    ret,frame = cap.read()
    if not ret:
        print('cannot grab frame from camera')
        continue
    results = decode(frame)
    for result in results:
        print('barcode = %s' % result.data)
        barcode_roi = frame[result.rect.left:result.rect.width,result.rect.top:result.rect.height]
        cv2.imshow('barcode:%s' % result.data,barcode_roi)

    cv2.imshow('camera',frame)
    key = cv2.waitKey(10)
    if key == 27:
        break

cv2.destroyAllWindows()

# from sys import argv  
# import zbar  
# import Image  
# img_file="datas/barcode-3.jpg"

# # 创建扫描器实例
# scanner = zbar.ImageScanner()  
# # 设置 
# scanner.parse_config('enable')  
# # 读取条码图片
# pil=Image.open(img_file).conver('L')  
# width, height = pil.size  
# raw = pil.tostring()  
# # 转换成可识别的格式
# image = zbar.Image(width, height, 'Y800', raw)  
# # 识别条码  
# scanner.scan(image)  
# # 获取识别结果
# for symbol in image:  
#     # do something useful with results  
#     print('decoded', symbol.type, 'symbol', '"%s"' % symbol.data)
  
# # clean up  
# del(image)  