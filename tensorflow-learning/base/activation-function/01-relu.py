import tensorflow as tf

arr = [-3.0 , 0.0 , 3.0]

initialize_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(initialize_op)
    res = sess.run(tf.nn.relu(arr))
    print(res)
    res = sess.run(tf.nn.relu6([-10 , 0 , 10]))
    print(res)