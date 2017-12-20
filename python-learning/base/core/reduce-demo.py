# -*- coding: utf-8 -*-

from functools import reduce

def f(x,y):
    return x + y

A = range(1,100)

B = reduce(f,A)

print(B)