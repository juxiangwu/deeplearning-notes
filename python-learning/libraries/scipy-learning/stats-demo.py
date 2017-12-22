# -*- coding: utf-8 -*-

import numpy as np
import scipy
from scipy import stats

scores = np.array([114, 100, 104, 89, 102, 91, 114, 114, 103, 105, 
108, 130, 120, 132, 111, 128, 118, 119, 86, 72, 111, 103, 74, 112, 107, 
103, 98, 96, 112, 112, 93])


xmean = scipy.mean(scores)
print(xmean)
sigma = scipy.std(scores)
print(sigma)

result = scipy.stats.bayes_mvs(scores)
print(result)