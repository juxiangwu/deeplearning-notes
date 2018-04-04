#coding:utf-8
'''
删除序列中重复元素
'''

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(set(a))

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
res = list(dedupe(a, key=lambda d: (d['x'],d['y'])))
print(res)

b = [1, 5, 2, 1, 9, 1, 5, 10]
res = list(dedupe(b))
print(res)
