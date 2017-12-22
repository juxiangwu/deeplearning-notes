# -*- coding: utf-8 -*-

import numpy
import scipy.sparse

rows=numpy.array([0,1,2,3])
cols=numpy.array([1,2,3,4])
vals=numpy.array([10,20,30,40])

A=scipy.sparse.coo_matrix( (vals,(rows,cols)) )
print (A); print (A.todense())
