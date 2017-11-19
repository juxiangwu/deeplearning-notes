# -*- coding: utf-8 -*-
import tensorflow as tf

from numpy.random import RandomState

batch_size = 8

w1 = tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2 = tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

x = tf.placeholder(tf.float32,shape=(None,2),name='x-input')
y_ = tf.placeholder(tf.float32,shape=(None,1),name='y-input')

a = tf.matmul(x,w1)
y = tf.matmul(a,w2)

cross_entropy = -tf.reduce_mean(y_ * tf.log(tf.clip_by_value(y,1e-10,1.0)))
train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)

rdm = RandomState(1)
dataset_size = 8
X = rdm.rand(dataset_size,2)
Y = [[int(x1+x2 < 1)] for (x1,x2) in X]

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)
    
    w1 = [[-0.81131822,1.48459876,0.06532937],
          [-2.44270396,0.0992484,0.59122431]]
    
    w2 = [[-0.81131822],[1.48459876],[0.06532937]]
    
    STEP = 5000
    
    for i in range(STEP):
        start = (i * batch_size) % dataset_size
        end = min(start+batch_size,dataset_size)
        
        sess.run(train_step,feed_dict={x:X[start:end],y_:Y[start:end]})
        
        if i % 100 == 0:
            total_loss_entropy = sess.run(cross_entropy,feed_dict={x:X,y_:Y})
            print('After %d training step(s),cross entropy on all data is %g' % (i,total_loss_entropy))
    
    print(sess.run(w1))
    print(sess.run(w2))