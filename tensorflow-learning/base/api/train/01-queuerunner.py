# -*- coding:utf-8 -*-

import numpy as np
import tensorflow as tf

q = tf.FIFOQueue(1000,'float')
counter = tf.Variable(0.0)
increment_op = tf.assign_add(counter,tf.constant(1.0))
enqueue_op = q.enqueue(counter)

qr = tf.train.QueueRunner(q,enqueue_ops = [increment_op,enqueue_op] * 1)

init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    enqueue_threads = qr.create_threads(sess,start = True)

    for i in range(10):
        print(sess.run(q.dequeue()))