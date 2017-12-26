# -*- coding: utf-8 -*-

'''
类型转换
'''

import numpy as np
from sklearn import random_projection

rng = np.random.RandomState(0)
X = rng.rand(10,2000)
X = np.array(X,dtype='float32')
print(X.dtype)

transformer = random_projection.GaussianRandomProjection()
X_new = transformer.fit_transform(X)
print(X_new.dtype)
