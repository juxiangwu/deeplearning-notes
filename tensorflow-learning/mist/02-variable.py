# -*- coding: utf-8 -*-
import tensorflow as tf

state = tf.Variable(0,name='conunter')

one = tf.constant(1)

new_value = tf.add(state,one)
#update_value = tf.assign(value=new_value);

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(new_value))

