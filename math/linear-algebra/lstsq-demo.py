# -*- coding: utf-8 -*-
'''
最小二乘法
'''

import numpy
import scipy
import scipy.linalg

A = numpy.mat(numpy.eye(3,k = 1))

b = numpy.mat(numpy.arange(3) + 1).T

xinfo = scipy.linalg.lstsq(A,b)

print(xinfo[0].T)