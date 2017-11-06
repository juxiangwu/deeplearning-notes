# -*- coding: utf-8 -*-

import tensorflow as tf
# 装在MNIST数据
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("../../datas/mnist", one_hot=True)

# 一些参数
learning_rate = 0.01
training_epochs = 25
batch_size = 100
display_step = 1

# tf Graph Input
x = tf.placeholder(tf.float32, [None, 784]) # mnist图像数据 28*28=784
y = tf.placeholder(tf.float32, [None, 10]) # 图像类别，总共10类

# 设置模型参数变量w和b
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

# 构建softmax模型
pred = tf.nn.softmax(tf.matmul(x, W) + b)


# 损失函数用cross entropy
cost = tf.reduce_mean(-tf.reduce_sum(y*tf.log(pred), reduction_indices=1))
# 梯度下降优化
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# 初始化所有变量
init = tf.global_variables_initializer()

# Launch the graph
with tf.Session() as sess:
    sess.run(init)
    # Training cycle
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(mnist.train.num_examples/batch_size)
        # 每一轮迭代total_batches
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            # 使用batch data训练数据
            _, c = sess.run([optimizer, cost], feed_dict={x: batch_xs,
                                                          y: batch_ys})
            # 将每个batch的损失相加求平均
            avg_cost += c / total_batch
        # 每一轮打印损失
        if (epoch+1) % display_step == 0:
            print ("Epoch:", '%04d' % (epoch+1), "cost=", "{:.9f}".format(avg_cost))

    print ("Optimization Finished!")

    # 模型预测
    # tf.argmax(pred,axis=1)是预测值每一行最大值的索引，这里最大值是概率最大
    # tf.argmax(y,axis=1)是真实值的每一行最大值得索引，这里最大值就是1
    correct_prediction = tf.equal(tf.argmax(pred, 1), tf.argmax(y, 1))

    # 对3000个数据预测准确率
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    print ("Accuracy:", accuracy.eval({x: mnist.test.images[:3000], y: mnist.test.labels[:3000]}))