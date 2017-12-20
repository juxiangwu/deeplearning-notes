# -*- coding: utf-8 -*-

import pickle

d = dict(name="Bob",age=24,score=80)
value = pickle.dumps(d)
print(value)

f = open('dumps.dat','wb')
pickle.dump(d,f)
f.close()

f = open('dumps.dat','rb')
d = pickle.load(f)
print(d)
f.close()