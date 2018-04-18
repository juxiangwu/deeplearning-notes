#coding:utf-8
'''
众数
'''
from collections import Counter
def mode(v):
    counts = Counter(v)
    max_count = max(counts.values())
    return [x_i for x_i,count in counts.items() if count == max_count]


v = [7,1,7,2,7,2,2,7,3,4,5,5,6,7,7,7,7,8,8,8,8,8,8]
print('mode:',mode(v))