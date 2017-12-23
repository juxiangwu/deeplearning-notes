# -*- coding: utf-8 -*-

'''
回归
'''
import numpy
import scipy
import matplotlib.pyplot as plt 

x = numpy.linspace(0,1,10)
y = numpy.sin(x * numpy.pi / 2)

line = numpy.polyfit(x,y,deg = 1)
plt.plot(x,y,'.',x,numpy.polyval(line,x),'r')
plt.show()
