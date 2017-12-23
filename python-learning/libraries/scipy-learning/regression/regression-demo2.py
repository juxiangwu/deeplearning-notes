# -*- coding: utf-8 -*-

import numpy
import scipy.interpolate
import matplotlib.pyplot as plt 

x = numpy.linspace(0,1,10)
y = numpy.sin(x * numpy.pi / 2)
spline = scipy.interpolate.UnivariateSpline(x,y,k = 2)

xn = numpy.linspace(0,1,100)
plt.plot(x,y,'.',xn,spline(xn))
plt.show()