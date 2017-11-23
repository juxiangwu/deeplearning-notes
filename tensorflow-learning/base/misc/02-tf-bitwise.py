# -*- coding: utf-8 -*-

import tensorflow as tf


init_op = tf.global_variables_initializer()

a = tf.constant([1,0,1,1])
b = tf.constant([0,1,1,0])

with tf.Session() as sess:
    sess.run(init_op)
    
    a_xor_b = tf.bitwise.bitwise_xor(a,b)
    a_and_b = tf.bitwise.bitwise_and(a,b)
    a_or_b = tf.bitwise.bitwise_or(a,b)
    a_inv = tf.bitwise.invert(a)
    print(sess.run(a_xor_b))
    print(sess.run(a_and_b))
    print(sess.run(a_or_b))
    print(sess.run(a_inv))
