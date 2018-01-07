# -*- coding: utf-8 -*-

'''
MNIST线性模型
'''

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#加载数据，"MNIST_data/"为路径，可自行更改，one_hot 独热，标记数组中的一个位0，其他为0，也就是统计中的虚拟编码
mnist = input_data.read_data_sets("temp/mnist/", one_hot=True)

#构建回归模型，输入原始真实值（group truth）,采用sotfmax函数拟合，并定义损失函数和优化器

#定义回归模型
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.matmul(x, W) + b #  预测值=矩阵运算(输入，权值) + 偏置

# 定义损失函数和优化器

y_ = tf.placeholder(tf.float32, [None, 10]) #输入真实占位符

#使用tf.nn.softmax_cross_entropy_with_logits计算预测值与真实值之间的差距
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y))
#使用梯度下降优化
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

#训练模型
#使用InteractiveSession()创建交互式上下文tf会话，这里的会话是默认
#在tf.Tensor.eval 和tf.Operation.run中都可以使用该会话来运行操作(OP)
sess = tf.InteractiveSession()
#注意：之前的版本中使用的是 tf.initialize_all_variables 作为初始化全局变量，已被弃用，更新后的采用一下命令
tf.global_variables_initializer().run()


for _ in range(1000):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

#模型评估
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1)) # 计算预测模型和真实值
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32)) # 布尔型转化为浮点数，并取平均值 ，得出准确率
#计算模型在测试集上的准确率 并打印结果
print(sess.run(accuracy, feed_dict={x: mnist.test.images,
                                      y_: mnist.test.labels}))