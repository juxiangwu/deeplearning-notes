# -*- coding:utf-8 -*-

import numpy as np
import tensorflow as tf

a = tf.constant([[-1.0,2.0,3.0,4.0]])

init_opt = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_opt)
    res = tf.nn.dropout(a,0.5,noise_shape=[1,4])
    result = sess.run(res)
    print(result)
    res = tf.nn.dropout(a,0.5,noise_shape=[1,1])
    result = sess.run(res)
    print(result)