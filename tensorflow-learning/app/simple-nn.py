# -*- coding: utf-8 -*-

'''
拟合f(x) = x^2 -0.5
'''

import numpy as np
import tensorflow as tf

# 构造函数数据
x_data = np.linspace(-1,1,300)[:,np.newaxis]

# 噪声数据
nose_data = np.random.normal(0,0.05,x_data.shape)

# 构造函数
y_data = np.square(x_data) - 0.5 + nose_data

# 定义神经网络数据
xs = tf.placeholder(tf.float32,[None,1])
ys = tf.placeholder(tf.float32,[None,1])

# 构建神经网络
# 每一层都经过向量化处理 y = weight * x + bias
def add_layer(inputs,in_size,out_size,activation_func=None):
    # 构建权重weights = in_size * out_size 矩阵
    weights = tf.Variable(tf.random_normal([in_size,out_size]))
    # 构建 biases = 1*out_size矩阵
    biases = tf.Variable(tf.random_normal([1,out_size]) + 0.1)

    # 矩阵相乘
    Wx_plus_b = tf.matmul(inputs,weights) + biases

    if activation_func == None:
        return Wx_plus_b
    else:
        outputs = activation_func(Wx_plus_b)
    return outputs

# 构建隐藏层
h1 = add_layer(xs,1,20,activation_func=tf.nn.relu)

# 构建输出层
pred = add_layer(h1,20,1,activation_func=None)

# 构建损失函数
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - pred),reduction_indices=[1]))
# 构建优化器
optimizer = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

# 训练神经网络
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    for i in range(1000):
        sess.run(optimizer,feed_dict={xs:x_data,ys:y_data})
        if i % 10 == 0:
            output = sess.run(loss,feed_dict={xs:x_data,ys:y_data})
            print(output)
    print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
    
