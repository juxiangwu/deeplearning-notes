# -*- coding:utf-8 -*-

# 显示随机数据
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

data = tf.random_normal([2,20])

sess = tf.Session()

out = sess.run(data)
x,y = out

plt.scatter(x,y)

plt.show()

sess.close()