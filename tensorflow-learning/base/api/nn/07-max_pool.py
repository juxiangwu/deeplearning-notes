# -*- coding:utf-8 -*-

import numpy as np
import tensorflow as tf

input_data = tf.Variable(np.random.rand(10,6,6,3),dtype=np.float32)
filter_data = tf.Variable(np.random.rand(2,2,3,10),dtype = np.float32)

y = tf.nn.atrous_conv2d(input_data,filter_data,2,padding='SAME')
output = tf.nn.max_pool(value=y,ksize=[1,2,2,1],strides=[1,1,1,1],padding='SAME')
init_opt = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_opt)
    res = sess.run(output)
    print('conv2d:\n',res)