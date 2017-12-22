# -*- coding: utf-8 -*-

'''
简单绘制
'''

import numpy as np
import matplotlib.pyplot as plt 

x = np.linspace(0,2 * np.pi,32)
fig = plt.figure()
plt.plot(x,np.sin(x))
plt.show()
plt.savefig('temp/sing.png')