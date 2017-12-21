# -*- coding: utf-8 -*-

'''
折半查找
'''

def bin_search(array,key,low,high):
    mid = int((low + high) // 2)
    if key == array[mid]:
        return True
    if low > high:
        return False
    if key < array[mid]:
        return bin_search(array,key,low,mid - 1)
    if key > array[mid]:
        return bin_search(array,key,mid + 1,high)

if __name__ == '__main__':
    datas = [0,10,9,-5,8,11,-10,1,10,-90]
    print(bin_search(datas,110,0,len(datas) - 1))