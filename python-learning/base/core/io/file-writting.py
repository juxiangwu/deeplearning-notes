# -*- coding: utf-8 -*-
import os
filename = os.path.realpath(os.path.join(os.getcwd(),'datas/test.dat'))
f = open(filename,'w')
data = {'name':'jenson','age':'29'}
f.write(str(data))

print(str(data))
f.close()