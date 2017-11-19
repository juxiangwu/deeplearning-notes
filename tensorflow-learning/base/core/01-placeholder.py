import tensorflow as tf
import numpy as np

arr = np.array([1.0 , 2.0 , 3.0 , 4.0 , 5.0 , 6.0 , 7.0 , 8.0 ,9.0],np.float32)
x_data = tf.placeholder(tf.float32)
x_constant = tf.constant(3.0)
x_product = tf.multiply(x_data , x_constant)
initialize_op = tf.global_variables_initializer()

my_array = np.array([
    [1., 3., 5., 7., 9.],
    [-2., 0., 2., 4., 6.],
    [-6., -3., 0., 3., 6.]
    ])
x_vals = np.array([my_array, my_array + 1])
x_data2 = tf.placeholder(tf.float32, shape=(3, 5))
m1 = tf.constant([[1.],[0.],[-1.],[2.],[4.]])
m2 = tf.constant([[2.]])
a1 = tf.constant([[10.]])

prod1 = tf.matmul(x_data, m1)
prod2 = tf.matmul(prod1, m2)
add1 = tf.add(prod2, a1)



with tf.Session() as sess:
    sess.run(initialize_op)
    for value in arr:
        res = sess.run(x_product,feed_dict={x_data:value})
        print(res)
    for x_val in x_vals:
        print(sess.run(add1, feed_dict={x_data: x_val}))