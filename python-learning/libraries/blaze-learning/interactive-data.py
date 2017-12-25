# -*- coding: utf-8 -*-

import blaze

t = blaze.data([(1, 'Alice', 100),
(2, 'Bob', -200),
(3, 'Charlie', 300),
(4, 'Denis', 400),
(5, 'Edith', -500)],fields = ['id','name','balance'])

#print(t.peek())
print(t[t.balance < 0])