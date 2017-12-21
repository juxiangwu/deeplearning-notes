# -*- coding: utf-8 -*-

'''
Shell排序
'''

def shell_sort(lists):
    count = len(lists)
    step = 2
    group = count // step
    while group > 0:
        for i in range(0,group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group //= step
    return lists


if __name__ == '__main__':
    datas = [0,10,9,-5,8,11,-10,1,10,-90]
    print(shell_sort(datas))