# -*- coding: utf-8 -*-

'''
插入排序
'''

def inser_sort(datas):
    count = len(datas)
    for i in range(count):
        key = datas[i]
        j = i - 1
        while j >= 0 :
            if datas[j] > key:
                datas[j + 1] = datas[j]
                datas[j] = key
            j -= 1
    return datas

if __name__ == '__main__':
    datas = [0,10,9,-5,8,11,-10]
    print(inser_sort(datas))