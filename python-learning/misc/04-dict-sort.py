# coding:utf-8
'''
字典排序
'''
prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}
# 对字典操作通过zip函数将键和值反转
price_sorted = sorted(zip(prices.values(),prices.keys()))

print(price_sorted)