# -*- coding: utf-8 -*-
'''
列表
'''
#创建大小为5的列表
A = [None] * 5
print(len(A))

A[0] = 'A'
A[1] = 'B'
A[2] = 'C'
A[3] = 'D'
A[4] = 'E'

print(A)

A.append('Apple')
A.append('Orange')
print('leng of list A = %d' % len(A))

A.insert(1,'Good')
print('Len = %d' % len(A))
print(A)

A.insert(0,[1,2,3])
print('Len = %d' % len(A))
print(A)

print(A.pop())
print('Len = %d' % len(A))
print(A)

print(A[1:3])
