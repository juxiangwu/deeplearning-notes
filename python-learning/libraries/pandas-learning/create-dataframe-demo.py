# -*- coding: utf-8 -*-

'''
创建数据帧
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range('20130101',periods=6)

df = pd.DataFrame(np.random.rand(6,4),index=dates,columns=['A','B','C','D'])

print(df)

df2 = pd.DataFrame({'A':1.0,
                    'B':pd.Timestamp('20130102'),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([3] * 4,dtype='int32'),
                    'E':pd.Categorical(["test","train","test","train"]),
                    'F':'foo'})
print(df2)


print('head:\n',df.head())
print('tail:\n',df.tail(3))
print('A = \n',df['A'])
print('loc:\n',df.loc['20130102':'20130104',['A','B']])

#plt.figure()
df.plot()
plt.legend(loc='best')
plt.show()