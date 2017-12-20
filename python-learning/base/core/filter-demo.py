# -*- coding: utf-8 -*-

def is_odd(x):
    return x % 2 == 1

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x : x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

A = list(filter(is_odd,range(1,100)))
print(A)


    
