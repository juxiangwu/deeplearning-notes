# -*- coding: utf-8 -*-
import numpy
import theano
import theano.tensor as T
from theano import function

x = T.dscalar('x')
y = T.dscalar('y')

z = x + y
f = function([x,y],z)

val = f(2,3)
print(val)
x1 = T.dmatrix('x')
y1 = T.dmatrix('y')
z1 = x1 + y1
f1 = function([x1,y1],z1)

m = f1([[1, 2], [3, 4]], [[10, 20], [30, 40]])
print(m)

a = T.vector()  # declare variable  
b = T.vector()  # declare variable  
out = a ** 2 + b ** 2 + 2 * a * b  # build symbolic expression  
f2 = function([a, b], out)   # compile function  
print(f2([1, 2], [4, 5]))  # prints [ 25.  49.]  