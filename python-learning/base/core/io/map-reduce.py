# -*- coding: utf-8 -*-
from functools import reduce
def f(x):
    return x * x

a = [1,2,4,5,6,7,8,9,10]

r = map(f,a)
print(list(r))

def f2(x1,x2):
    return x1 * x2

r2 = reduce(f2,a)
print(r2)

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print(str2int('12345'))