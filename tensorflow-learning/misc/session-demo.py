# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np

m1 = tf.constant([[3,3]])
m2 = tf.constant([[2],[2]])

res_m1 = m1 * m2
res_m2 = tf.matmul(m1,m2)

init = tf.initialize_all_variables()

sess = tf.Session()

sess.run(init)

print(sess.run(res_m1))
print(sess.run(res_m2))

sess.close()