# -*- coding: utf-8 -*-

import tensorflow as tf

w1 = tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2 = tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

x = tf.constant([[0.7,0.9]])

a = tf.matmul(x,w1)
y = tf.matmul(a,w2)

sess = tf.Session()

init_op = tf.global_variables_initializer()

sess.run(init_op)

res = sess.run(y)

print(res)

sess.close()