#coding:utf-8
'''
单变量方程求解
'''
import scipy
from scipy import optimize
import numpy as np
# 使用bisection法
result = optimize.bisect(lambda x: np.exp(x) - 2, -2, 2)
print('result=',result)

# 使用Newton法
x_root_guess = 2
f = lambda x: np.exp(x) - 2
fprime = lambda x: np.exp(x)
result = optimize.newton(f, x_root_guess)
print('result = ',result)
result = optimize.newton(f, x_root_guess, fprime=fprime)
print('result = ',result)

# 使用混合方法
result = optimize.brentq(lambda x: np.exp(x) - 2, -2, 2)
print('result = ',result)
result = optimize.brenth(lambda x: np.exp(x) - 2, -2, 2)
print('result = ',result)
