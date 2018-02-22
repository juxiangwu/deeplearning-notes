#coding:utf-8
'''
N次一元方程求解
'''
import tensorflow as tf
import numpy as np

tf.logging.set_verbosity(tf.logging.ERROR)              #日志级别设置成 ERROR，避免干扰
np.set_printoptions(threshold='nan')                    #打印内容不限制长度

t_x = np.floor(10 * np.random.random([5]),dtype=np.float32)
print(t_x)

t_y = t_x * 3.0 +8.0
print(t_y)

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
a = tf.Variable(0.0)
b = tf.Variable(0.0)
curr_y = x*a+b

loss = tf.reduce_sum(tf.square(curr_y - y))             #损失函数，实际输出数据和训练输出数据的方差
optimizer = tf.train.GradientDescentOptimizer(0.001)
train = optimizer.minimize(loss)                        #训练的结果是使得损失函数最小

sess = tf.Session()                                     #创建 Session
sess.run(tf.global_variables_initializer())             #变量初始化

for i in range(10000):
        sess.run(train, {x:t_x, y:t_y})
        print(sess.run([a,b,loss],{x:t_x, y:t_y}))