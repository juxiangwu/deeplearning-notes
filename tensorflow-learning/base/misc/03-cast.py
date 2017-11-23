# -*- coding: utf-8 -*-

'''
Tensorflow 类型转换
'''

import tensorflow as tf

init = tf.global_variables_initializer()

a = "123.0"

b = tf.constant("234.4")


with tf.Session() as sess:
    sess.run(init)
    
    print(sess.run(tf.string_to_number(a)))
    print(sess.run(tf.string_to_number(b)))