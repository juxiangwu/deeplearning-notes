#coding:utf-8
'''
标准正态分布
'''

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

def normal_distribution(x,mean,sigma):
    result = tf.exp(tf.negative(tf.pow(x-mean, 2.0) / (2.0 * tf.pow(sigma, 2.0) ))) *(1.0 / (sigma * tf.sqrt(2.0 * np.pi) ))
    return result


x = np.arange(1,100,dtype=np.float32)
result = normal_distribution(x,0.0,2.0)

sess = tf.Session()
init_op = tf.global_variables_initializer()
sess.run(init_op)
res = sess.run(result)
# print(res)
sess.close()

plt.plot(np.arange(1,100),res)
plt.show()