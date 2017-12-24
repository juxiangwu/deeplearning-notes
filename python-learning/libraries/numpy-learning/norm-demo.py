# -*- coding: utf-8 -*-
'''
向量范数
'''
import numpy as np 
A = [8,1,6]

modA = np.sqrt(np.sum(np.power(A,2)))

print('modA:\n',modA)

normA = np.linalg.norm(A)
print('normA:\n',normA)