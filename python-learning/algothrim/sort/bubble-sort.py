# -*- coding: utf-8 -*-

'''
冒泡排序
'''

def bubble_sort(lists):
    count = len(lists)
    for i in range(0,count):
        for j in range(i + 1,count):
            if lists[i] > lists[j]:
                lists[i],lists[j] = lists[j],lists[i]
    return lists

if __name__ == '__main__':
    datas = [0,10,9,-5,8,11,-10,1,10,-90]
    print(bubble_sort(datas))