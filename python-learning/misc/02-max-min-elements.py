#coding:utf-8
'''
查找最大或最小N个元素
'''
import heapq

datas = [1,2,3,4,5,6,7,-9,10,-11,15,17,-20]

# 前最大3个元素
print(heapq.nlargest(3,datas))
# 前最小5个元素
print(heapq.nsmallest(5,datas))

datas2 = [
    {"name":"XiaoMi","price":2999},
    {"name":"Huawei","price":4999},
    {"name":"iPhone","price":8999},
    {"name":"Vivo","price":1099},
    {"name":"oppo","price":2499},
    {"name":"Lenovo","price":1999}
]

# 复杂结构查找
cheap = heapq.nsmallest(3,datas2,key = lambda s:s['price'])
print(cheap)

# portfolio = [
# {'name': 'IBM', 'shares': 100, 'price': 91.1},
# {'name': 'AAPL', 'shares': 50, 'price': 543.22},
# {'name': 'FB', 'shares': 200, 'price': 21.09},
# {'name': 'HPQ', 'shares': 35, 'price': 31.75},
# {'name': 'YHOO', 'shares': 45, 'price': 16.35},
# {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
# print(cheap)
# expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
# print(expensive)