# -*- coding:utf-8 -*-

import numpy as np
import tensorflow as tf

x = tf.random_normal(shape = [1,3,3,1])
kernel = tf.random_normal(shape = [2,2,3,1])
y = tf.nn.conv2d_transpose(x,kernel,output_shape=[1,5,5,3],strides=[1,2,2,1],padding="SAME")

init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    res = sess.run(y)
    print(res)