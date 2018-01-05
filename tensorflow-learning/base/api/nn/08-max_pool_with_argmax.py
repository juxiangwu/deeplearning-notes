# -*- coding:utf-8 -*-

import numpy as np
import tensorflow as tf

input_data = tf.Variable(np.random.rand(10,6,6,3),dtype=np.float32)
filter_data = tf.Variable(np.random.rand(2,2,3,10),dtype = np.float32)


init_opt = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_opt)
    y = tf.nn.conv2d(input_data,filter_data,strides=[1,1,1,1],padding='SAME')
    output,argmax = tf.nn.max_pool_with_argmax(input=y,ksize=[1,2,2,1],strides=[1,1,1,1],padding='SAME')
    print('conv2d:\n',output)