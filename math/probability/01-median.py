#coding:utf-8
'''
中位数
'''
def median(v):
    n = len(v)
    sorted_v = sorted(v)
    median_point = n // 2

    if n % 2 == 0:
        # 偶数，返回中间两个均值
        lft = median_point = -1
        rgt = median_point
        return (sorted_v[lft] + sorted_v[rgt]) / 2
    else:
        return sorted_v[median_point]

v = [1,2,-3,4,5,8]
print(median(v))

v2 = [1,3,4,5,-10,-8,-1]
print(median(v2))