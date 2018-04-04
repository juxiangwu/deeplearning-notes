# coding:utf-8
'''
矩阵操作
'''

def shape(A):
    rows = len(A)
    cols = len(A[0]) if A else 0
    return rows,cols

def get_row(A,i):
    return A[i]

def get_column(A,j):
    return [A_i[j] for A_i in A]

def make_matrix(rows,cols,entry_fun):
    return[[entry_fun(i,j) for j in range(cols)] for i in range(rows)]

def is_diagonal(i,j):
    return 1 if i == j else 0

A = [[1,2,3],[4,5,6],[7,8,9]]

print('shape:',shape(A))
print('get_row:',get_row(A,1))
print('get_column:',get_column(A,2))
print('make matrix:\n',make_matrix(5,5,is_diagonal))
