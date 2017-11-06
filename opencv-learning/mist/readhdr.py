# -*- coding: utf-8 -*-
import cv2
import numpy as np
def rgbe2float(rgbe):
    res = np.zeros((rgbe.shape[0],rgbe.shape[1],3))
    p = rgbe[:,:,3]>0
    m = 2.0**(rgbe[:,:,3][p]-136.0)
    res[:,:,0][p] = rgbe[:,:,0][p] * m
    res[:,:,1][p] = rgbe[:,:,1][p] * m
    res[:,:,2][p] = rgbe[:,:,2][p] * m
    return res
     
     
def readHdr(fileName = 'belgium.hdr'):
    fileinfo = {}
    with open(fileName, 'rb') as fd:
        tline = fd.readline().strip()
        if len(tline)<3 or tline[:2] != '#?':
            print ('invalid header')
            return 
        fileinfo['identifier'] = tline[2:]
 
        tline = fd.readline().strip()
        while tline:
            n = tline.find('=')
            if n>0:
                fileinfo[tline[:n].strip()] = tline[n+1:].strip()
            tline = fd.readline().strip()
 
        tline = fd.readline().strip().split(' ')
        fileinfo['Ysign'] = tline[0][0]
        fileinfo['height'] = int(tline[1])
        fileinfo['Xsign'] = tline[2][0]
        fileinfo['width'] = int(tline[3])
 
        data = [ord(d) for d in fd.read()]
        height, width = fileinfo['height'], fileinfo['width']
        if width<8 or width>32767:
            data.resize((height, width, 4))
            return rgbe2float(data)
 
        img = np.zeros((height, width, 4))
        dp = 0
        for h in range(height):
            if data[dp] !=2 or data[dp+1]!=2:
                print 'this file is not run length encoded'
                print data[dp:dp+4]
                return
            if data[dp+2]*256+ data[dp+3] != width:
                print 'wrong scanline width'
                return
            dp += 4
            for i in range(4):
                ptr = 0
                while(ptr < width):
                    if data[dp]>128:
                        count = data[dp]-128
                        if count==0 or count>width-ptr:
                            print 'bad scanline data'
                        img[h, ptr:ptr+count,i] = data[dp+1]
                        ptr += count
                        dp += 2
                    else:
                        count = data[dp]
                        dp += 1
                        if count==0 or count>width-ptr:
                            print 'bad scanline data'
                        img[h, ptr:ptr+count,i] = data[dp: dp+count]
                        ptr += count
                        dp +=count
        return rgbe2float(img)
if __name__ == '__main__':
    m = readHdr()
    m1,m2 = m.max(), m.min()
    img = (m-m2)/(m1-m2)
    m1 = m[:,:,0].copy();  m[:,:,0] = m[:,:,2]; m[:,:,2]=m1
    cv2.imwrite('tmp.jpg', img*255)
