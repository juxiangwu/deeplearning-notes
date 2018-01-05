# -*- coding:utf-8 -*-

import numpy as np
import tensorflow as tf

q = tf.FIFOQueue(3,'float')
init = q.enqueue(([0.1,0.2,0.3],))
init_opt = tf.global_variables_initializer()
x = q.dequeue()
y = x + 1
q_inc = q.enqueue([y])

with tf.Session() as sess:
    sess.run(init_opt)
    sess.run(init)
    qlen = sess.run(q.size())
    for i in range(2):
        sess.run(q_inc)
    qlen = sess.run(q.size())
    for i in range(qlen):
        print(sess.run(q.dequeue()))
