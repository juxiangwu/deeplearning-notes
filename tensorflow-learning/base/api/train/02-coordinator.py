# -*- coding:utf-8 -*-

import numpy as np
import tensorflow as tf

# 主线程
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# Coordinator:协调器
coord = tf.train.Coordinator()

#忘却 入队线程，协调器是函数的参数
qr = tf.train.QueueRunner(q,enqueue_ops = [increment_op,enqueue_op] * 1)
enqueue_threads = qr.create_threads(sess,coord=coord,start=True)

coord.request_stop()

# 主线程
for i in range(0,10):
    try:
        print(sess.run(q.dequeue()))
    except tf.errors.OutOfRange:
        break
    
coord.join(enqueue_threads)