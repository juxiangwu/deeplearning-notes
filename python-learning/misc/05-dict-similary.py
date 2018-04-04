#coding:utf-8
'''
查找字典相同部分
'''

a = {
'x' : 1,
'y' : 2,
'z' : 3
}

b = {
'w' : 10,
'x' : 11,
'y' : 2
}

# 查找相同部分
print(a.keys() & b.keys())
print(a.items() & b.items())
# 查找不同部分
print(a.keys() - b.keys())

# 排除指定键
c = {key:a[key] for key in a.keys() - {'z','w'}}
print(c)