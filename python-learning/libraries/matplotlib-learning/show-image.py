# -*- coding: utf-8 -*-
import scipy.misc
img = scipy.misc.ascent()
import matplotlib.pyplot as plt 
plt.gray()
plt.imshow(img)
plt.show()
plt.savefig('temp/ascent.png')