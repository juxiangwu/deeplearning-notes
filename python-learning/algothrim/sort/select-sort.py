# -*- coding: utf-8 -*-

'''
选择排序
'''

def select_sort(lists):
    count = len(lists)
    for i in range(0,count):
        min = i
        for j in range(i + 1,count):
            if lists[min] > lists[j]:
                min = j
        lists[min],lists[i] = lists[i],lists[min]
    return lists

if __name__ == '__main__':
    datas = [0,10,9,-5,8,11,-10,1,10,-90]
    print(select_sort(datas))