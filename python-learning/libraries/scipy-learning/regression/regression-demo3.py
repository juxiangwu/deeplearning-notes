# -*- coding: utf-8 -*-

import numpy
import scipy

A = 18
w = 3 * numpy.pi
h = 0.5

x = numpy.linspace(0,1,100)
y = A * numpy.sin(w * x + h)
y += 4 * ((0.5 - scipy.rand(100)) * numpy.exp(2 * scipy.rand(100) ** 2))

import scipy.optimize
p0 = [20,2 * numpy.pi,1]
target_function = lambda x,AA,ww,hh:AA * numpy.sin(ww*x+hh)

pF,pVar = scipy.optimize.curve_fit(target_function,x,y,p0)
print(pF)

