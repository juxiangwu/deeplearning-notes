# -*- coding: utf-8 -*-

from pyzbar.pyzbar import decode
import cv2

img = cv2.imread('../datas/images/qrcode.png')

cv2.imshow("QRCode",img)

qrcode = decode(img)
if(len(qrcode) > 0):
    print(qrcode[0].data)

cv2.waitKey()
cv2.destroyAllWindows()