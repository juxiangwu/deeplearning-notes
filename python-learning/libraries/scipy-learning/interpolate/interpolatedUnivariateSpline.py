# -*- coding: utf-8 -*-
'''
多项式插值
'''

import numpy 
import matplotlib.pyplot as plt 
import scipy.interpolate

x = numpy.arange(5)
y = numpy.sin(x)
xn = numpy.linspace(0,4,40)

interp = scipy.interpolate.InterpolatedUnivariateSpline(x,y)
plt.plot(x,y,'.',xn,interp(xn))
plt.show()