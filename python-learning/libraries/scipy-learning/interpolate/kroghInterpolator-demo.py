# -*- coding: utf-8 -*-
import numpy
import matplotlib.pyplot as plt 
import scipy.interpolate

x = numpy.array([0,0,1,1,2,2])
y = numpy.array([0,0,1,0,2,0])

interp = scipy.interpolate.KroghInterpolator(x,y)
xn = numpy.linspace(0,2,20)

plt.plot(x,y,'o',xn,interp(xn),'r')
plt.show()