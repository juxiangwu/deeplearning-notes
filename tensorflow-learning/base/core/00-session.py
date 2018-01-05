# -*- coding:utf-8 -*-

import numpy as np
import tensorflow as tf


mat1 = tf.constant([[3.0,3.0]])
mat2 = tf.constant([[2.0],[2.0]])

product = tf.matmul(mat1,mat2)

with tf.Session() as sess:
    result = sess.run([product])
    print(result)