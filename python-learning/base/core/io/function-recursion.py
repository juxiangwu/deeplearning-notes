# -*- coding: utf-8 -*-

def fact_1(n):
    if n == 1:
        return 1
    return n * fact_1(n-1)

res = fact_1(512)
print(res)

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

res2 = fact(512)
print(res2)