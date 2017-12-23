# -*- coding: utf-8 -*-

import numpy
import matplotlib.pyplot as plt 

f = lambda x:[x[0] ** 2 - 2 * x[0] - x[1] + 0.5,x[0] ** 2 + 4 * x[1] ** 2- 4]

x,y = numpy.mgrid[-0.5:2.5:24j,-0.5:2.5:24j]
U,V = f([x,y])

plt.quiver(x,y,U,V,color='r' ,
        linewidths = (0.2,),edgecolor=('k'),
        headaxislength=5)
plt.show()