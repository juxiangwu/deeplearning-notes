# -*- coding: utf-8 -*-
import numpy
import scipy.interpolate
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

x = y = numpy.arange(10)
f = (lambda i,j:numpy.sin(i) * numpy.cos(j))
A = numpy.fromfunction(f,(10,10))

spline = scipy.interpolate.RectBivariateSpline(x,y,A)
fig = plt.figure()
subplot = fig.add_subplot(111,projection='3d')
xx = numpy.mgrid[0:9:100j,0:9:100j]
A = spline(numpy.linspace(0,9,100),numpy.linspace(0,9,100))
subplot.plot_surface(xx[0],xx[1],A)
plt.show()