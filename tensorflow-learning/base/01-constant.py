# -*- coding: utf-8 -*-

'''
  Tensorflow constant
'''

import tensorflow as tf

a = tf.constant(1)
b = tf.constant(2)

m1 = tf.constant([[1,2,3],[4,5,6]])
m2 = tf.constant([[7,8,9],[10,11,12]])
m3 = tf.constant([[2,2],[3,3],[4,4]])

m4 = tf.constant([[1,0,0],[0,1,0],[0,0,1]])
m5 = tf.constant([[1,2,3],[4,5,6],[7,8,9]])

c = a + b

mc = tf.add(m1,m2)

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    print(sess.run(c))
    print(sess.run(mc))
    print("m1 * m3 = " )
    print(sess.run(tf.matmul(m1,m3)))
    print("m4 * m5 = ")
    print(sess.run(tf.matmul(m4,m5)))
    print(sess.run(tf.matmul(m5,m4)))
    