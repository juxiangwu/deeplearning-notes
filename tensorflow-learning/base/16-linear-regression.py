# -*- coding: utf-8 -*-

# Tensorflow 线性回归演示

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.randn(2000,1)
w_real = 0.3
b_real = -0.2

NUM_STEPS = 10

noise = np.random.randn(2000,1) * 0.1
#y_data = np.matmul(w_real,x_data.T) + b_real #+ noise
y_data = x_data * w_real + b_real + noise
plt.scatter(x_data,y_data)
plt.show()

g = tf.Graph()
_wb = []

with g.as_default():
    x = tf.placeholder(tf.float32,shape=None)
    y_true = tf.placeholder(tf.float32,shape=None)
    
    with tf.name_scope('inference'):
        w = tf.Variable(0,dtype=tf.float32,name='weights')
        b = tf.Variable(0,dtype=tf.float32,name='bias')
        y_pred = x * w + b
        
    with tf.name_scope('loss'):
        loss = tf.reduce_mean(tf.square(y_true - y_pred))
        
    with tf.name_scope('train'):
        lr = 0.5
        optimizer = tf.train.GradientDescentOptimizer(lr)
        train = optimizer.minimize(loss)
        
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        for step in range(NUM_STEPS):
            sess.run(train,feed_dict={x:x_data,y_true:y_data})
            if (step % 5 == 0):
                print(step,sess.run([w,b]))
        print(sess.run([w,b]))
        