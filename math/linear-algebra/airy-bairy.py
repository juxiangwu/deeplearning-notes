# -*- coding: utf-8 -*-

import numpy
import scipy.special
import matplotlib.pyplot as plt 
import mpl_toolkits.mplot3d

x = numpy.mgrid[-4:4:100j,-4:4:100j]
z = x[0] + 1j * x[1]
(Ai,Aip,Bi,Bip) = scipy.special.airy(z)
steps = range(int(Bi.real.min()), int(Bi.real.max()),6)
fig=plt.figure()
subplot1=fig.add_subplot(121,aspect='equal')
subplot1.contourf(x[0], x[1], Bi.real, steps)
subplot2=fig.add_subplot(122,projection='3d')
subplot2.plot_surface(x[0],x[1],Bi.real)
plt.show()