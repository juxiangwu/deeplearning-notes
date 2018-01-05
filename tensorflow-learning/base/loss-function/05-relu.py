# -*- coding:utf-8 -*-

import numpy as np
import tensorflow as tf

a = tf.constant([[1.0,2.0],[1.0,2.0],[1.0,2.0]])
res = tf.nn.relu(a)
init_opt = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_opt)
    result = sess.run(res)
    print(result)