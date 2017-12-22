# -*- coding: utf-8 -*-

'''
多项式
'''
import numpy

P1 = numpy.poly1d([1,0,1])

print(P1)

#多项式的根
print(P1.r)
print(P1.o)
#多项式的导数
print(P1.deriv)