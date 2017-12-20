# -*- coding: utf-8 -*-
import os
fileName = os.path.realpath(os.path.join(os.getcwd(),'datas/test.bin'))
print(fileName)
print(fileName)
f  = open(fileName,'r')
for line in f:
    print(line)
f.close()