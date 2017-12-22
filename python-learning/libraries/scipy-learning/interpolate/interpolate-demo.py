# -*- coding: utf-8 -*-
'''
多项式插值
'''
import numpy
import matplotlib.pyplot as plt
import scipy.interpolate

x = numpy.linspace(-1,1,10)
xn = numpy.linspace(-1,1,1000)
y = numpy.sin(x)
polynomial = scipy.interpolate.lagrange(x,numpy.sin(x))
plt.plot(xn,polynomial(xn),x,y,'or')
plt.show()