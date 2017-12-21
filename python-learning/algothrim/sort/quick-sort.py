# -*- coding: utf-8 -*-

'''
快速排序
'''

def quick_sort(lists,left,right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right

    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists,low,left - 1)
    quick_sort(lists,left + 1,high)
    return lists

if __name__ == '__main__':
    datas = [0,10,9,-5,8,11,-10,1,10,-90]
    print(quick_sort(datas,0,len(datas)-1))