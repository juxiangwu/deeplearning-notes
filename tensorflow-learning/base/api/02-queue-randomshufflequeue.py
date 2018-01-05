# -*- coding:utf-8 -*-

import numpy as np
import tensorflow as tf

q = tf.RandomShuffleQueue(capacity=10,min_after_dequeue=2,dtypes="float")

with tf.Session() as sess:
    for i in range(0,10):
        sess.run(q.enqueue(i))

    for i in range(0,8):
        print(sess.run(q.dequeue()))