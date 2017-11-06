# -*- coding: utf-8 -*-

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("../../datas/mnist", one_hot=True)

# 产生随机变量，符合 normal 分布
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

# 产生常量矩阵
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

# 定义2维的convolutional图层
# strides：每跨多少步抽取信息，strides[1, x_movement,y_movement, 1]， [0]和strides[3]必须为1
# padding：边距处理，“SAME”表示输出图层和输入图层大小保持不变，设置为“VALID”时表示舍弃多余边距(丢失信息)
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

# 定义pooling图层
# pooling：解决跨步大时可能丢失一些信息的问题,max-pooling就是在前图层上依次不重合采样2*2的窗口最大值
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

x = tf.placeholder(tf.float32, [None, 784])
x_image = tf.reshape(x, [-1, 28, 28, 1])                   # 将原图reshape为4维，-1表示数据是黑白的，28*28=784，1表示颜色通道数目
y_ = tf.placeholder(tf.float32, [None, 10])

### 1. 第一层网络
# 把x_image的厚度由1增加到32，长宽由28*28缩小为14*14
W_conv1 = weight_variable([5, 5, 1, 32])                    # 按照[5,5,输入通道=1,输出通道=32]生成一组随机变量
b_conv1 = bias_variable([32])                               
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)    # 输出size 28*28*32(因为conv2d()中x和y步长都为1，边距保持不变)
h_pool1 = max_pool_2x2(h_conv1)                             # 输出size 14*14*32

### 2. 第二层网络
# 把h_pool1的厚度由32增加到64，长宽由14*14缩小为7*7
W_conv2 = weight_variable([5, 5, 32, 64]) 
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

### 3. 第一层全连接
# 把h_pool2由7*7*64，变成1024*1
W_fc1 = weight_variable([7*7*64, 1024])
b_fc1 = bias_variable([1024])
h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])               # 把pooling后的结构reshape为一维向量
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
keep_prob = tf.placeholder('float')
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)                   # 按照keep_prob的概率扔掉一些，为了减少过拟合 

### 4. 第二层全连接
#使用softmax计算概率进行分类， 最后一层网络，1024 -> 10， 
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)

cross_entropy = -tf.reduce_sum(y_ * tf.log(y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))

sess = tf.Session()
sess.run(tf.global_variables_initializer())
for i in range(20000):
    batch = mnist.train.next_batch(50)
    if i % 100 == 0:
        train_accuracy = accuracy.eval(session = sess, feed_dict={x: batch[0], y_: batch[1], keep_prob: 1.0})
        print ('step %d, training accuracy %g' % (i, train_accuracy))
    sess.run(train_step, feed_dict = {x: batch[0], y_: batch[1], keep_prob: 0.5})

print('test accuracy %g' % accuracy.eval(session = sess, feed_dict={x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))