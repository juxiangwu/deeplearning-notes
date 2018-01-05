# -*- coding:utf-8 -*-

import numpy as np
import tensorflow as tf

input_data = tf.Variable(np.random.rand(1,5,5,1),dtype=np.float32)
filter_data = tf.Variable(np.random.rand(3,3,1,1),dtype = np.float32)

y = tf.nn.atrous_conv2d(input_data,filter_data,2,padding='SAME')

init_opt = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_opt)
    res = sess.run(y)
    print('conv2d:\n',res)