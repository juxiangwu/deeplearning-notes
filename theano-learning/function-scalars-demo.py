# -*- coding:utf-8 -*-

import theano.tensor as T
from theano import function

a = T.scalar('a')
b = T.scalar('b')
c = T.scalar('c')
d = T.scalar('d')
e = T.scalar('e')

f = ((a - b + c) * d) / e

g = function([a,b,c,d,e],f)

print('Expected:((1 - 2 + 3) * 4) / 5',g(1,2,3,4,5))
