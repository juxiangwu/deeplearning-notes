# -*- coding:utf-8 -*-

import numpy as np
import tensorflow as tf

input_data = tf.Variable(np.random.rand(10,9,9,3),dtype=np.float32)
filter_data = tf.Variable(np.random.rand(2,2,3,2),dtype = np.float32)

y = tf.nn.conv2d(input_data,filter_data,strides=[1,1,1,1],padding='SAME')

init_opt = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_opt)
    res = sess.run(y)
    print('conv2d:\n',res)