# -*- coding: utf-8 -*-

import tensorflow as tf

v = tf.constant([[1.0,2.0,3.0],[4.0,5.0,6.0]])

#cross_entropy = -tf.reduce_mean(y_ * tf.log(tf.clip_by_value(y,1e-10,1.0)))

res = tf.clip_by_value(v,2.5,4.5);

init_op = tf.global_variables_initializer()

with tf.Session() as sess:
        print(sess.run(res))

