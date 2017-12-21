# -*- coding: utf-8 -*-

'''
基数排序
'''

import math

def radix_sort(lists,radix = 100):
    k = int(math.ceil(math.log(max(lists),radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1,k+1):
        for j in lists:
            print('index = %d' % (j // (radix ** (i - 1)) % (radix ** i)))
            bucket[j // (radix ** (i - 1)) % (radix ** i)].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists

if __name__ == '__main__':
    datas = [0,10,9,-5,8,11,-10,1,10,-90]
    print(radix_sort(datas))