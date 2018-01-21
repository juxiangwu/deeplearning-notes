# -*- coding:utf-8 -*-

# Name scope

import tensorflow as tf

with tf.name_scope('Scope_A'):
    a = tf.add(1,2,name="A_add")
    b = tf.multiply(a,3,name="A_mul")

with tf.name_scope("Scope_B"):
    c = tf.add(4,5,name="B_add")
    d = tf.multiply(c,6,name="B_mul")

e = tf.add(b,d,name="output")

with tf.Session() as sess:

    writer =tf.summary.FileWriter("temp/tensorboard/add_scope",
                                    graph = sess.graph)
    writer.close()

