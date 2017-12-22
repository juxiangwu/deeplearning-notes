# -*- coding: utf-8 -*-

'''
矩阵的特征值
'''

import numpy as np
import scipy.misc
from scipy.linalg import svd
import matplotlib.pyplot as plt 


img = scipy.misc.ascent()

U,s,Vh = svd(img)

A = np.dot(U[:,0:32],np.dot(np.diag(s[0:32]),Vh[0:32,:]))
plt.subplot(121,aspect='equal')
plt.imshow(img)
plt.gray()
plt.subplot(122,aspect='equal')
plt.imshow(A)
plt.show()