# -*- coding:utf-8 -*-

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
'''
MNIST无监督学习：自编码
'''
# 导入模块
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 加载数据
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("temp/mnist", one_hot=True)

#模型训练
# 设置超参数
learning_rate = 0.01 # 学习率
training_epochs = 20 # 训练轮数
batch_size = 64 # 每次训练的数据
display_step = 1 # 每隔多少轮显示一次训练结果
examples_to_show = 10 # 提示从测试集中选择10张图片取验证自动编码器的结果



# 网络参数
n_hidden_1 = 256 # 第一个隐藏层神经元个数（特征值格式）
n_hidden_2 = 128 # 第二个隐藏层神经元格式
n_input = 784 # 输入数据的特征个数  28*28=784
# 定义输入数据，无监督不需要标注数据，所以只有输入图片
X = tf.placeholder("float", [None, n_input])

#初始化每一层的权重和偏置
weights = {
    'encoder_h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'encoder_h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'decoder_h1': tf.Variable(tf.random_normal([n_hidden_2, n_hidden_1])),
    'decoder_h2': tf.Variable(tf.random_normal([n_hidden_1, n_input])),
}
biases = {
    'encoder_b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'encoder_b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'decoder_b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'decoder_b2': tf.Variable(tf.random_normal([n_input])),
}

#定义自动编码模型的网络结构，包括压缩和解压的过程

# 定义压缩函数
def encoder(x):
    # Encoder Hidden layer with sigmoid activation #1
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['encoder_h1']),
                                   biases['encoder_b1']))
    # Decoder Hidden layer with sigmoid activation #2
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['encoder_h2']),
                                   biases['encoder_b2']))
    return layer_2


# 定义解压函数
def decoder(x):
    # Encoder Hidden layer with sigmoid activation #1
    layer_1 = tf.nn.sigmoid(tf.add(tf.matmul(x, weights['decoder_h1']),
                                   biases['decoder_b1']))
    # Decoder Hidden layer with sigmoid activation #2
    layer_2 = tf.nn.sigmoid(tf.add(tf.matmul(layer_1, weights['decoder_h2']),
                                   biases['decoder_b2']))
    return layer_2

# 建立模型
encoder_op = encoder(X)
decoder_op = decoder(encoder_op)

# 得出预测分类值
y_pred = decoder_op
# 得出真实值，即输入值
y_true = X

# 定义损失函数和优化器
cost = tf.reduce_mean(tf.pow(y_true - y_pred, 2))
optimizer = tf.train.RMSPropOptimizer(learning_rate).minimize(cost)

# 初始化变量
init = tf.global_variables_initializer()

# 3 训练数据及评估模型
with tf.Session() as sess:
    sess.run(init)
    total_batch = int(mnist.train.num_examples/batch_size)
    # 开始训练
    for epoch in range(training_epochs):
        # Loop over all batches
        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            # Run optimization op (backprop) and cost op (to get loss value)
            _, c = sess.run([optimizer, cost], feed_dict={X: batch_xs})
        # 每一轮，打印一次损失值
        if epoch % display_step == 0:
            print("Epoch:", '%04d' % (epoch+1),
                  "cost=", "{:.9f}".format(c))

    print("Optimization Finished!")

    # 对测试集应用训练好的自动编码网络
    encode_decode = sess.run(
        y_pred, feed_dict={X: mnist.test.images[:examples_to_show]})
    # 比较测试集原始图片和自动编码网络的重建结果
    f, a = plt.subplots(2, 10, figsize=(10, 2))
    for i in range(examples_to_show):
        a[0][i].imshow(np.reshape(mnist.test.images[i], (28, 28)))
        a[1][i].imshow(np.reshape(encode_decode[i], (28, 28)))
    f.show()
    plt.draw()
    plt.waitforbuttonpress()