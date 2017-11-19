import tensorflow as tf

arr = [-3.0 , 0.0 , 3.0]

initialize_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(initialize_op)
    res = sess.run(tf.nn.tanh(arr))
    print(res)
