#coding:utf-8
'''
多项式
'''

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# 定义模型
def model(X,w):
    terms = []
    for i in range(num_coeffs):
        term = tf.multiply(w[i],tf.pow(X,i))
        terms.append(term)
    return tf.add_n(terms)

# 学习速率
learning_rate = 0.01

# 迭代次数
training_epochs = 40

# 生成模拟数据
train_X = np.linspace(-1,1,101)

# 设置多项式维度
num_coeffs = 6
train_Y_coeffs = [1,2,3,4,5,6]
train_Y = 0
for i in range(num_coeffs):
    train_Y += train_Y_coeffs[i] * np.power(train_X,i)

# 生成带有噪音的数据
train_Y += np.random.randn(*train_X.shape) * 1.5

# 定义训练参数
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

w = tf.Variable([0.] * num_coeffs,name='parameters')
y_model = model(X,w)

cost = (tf.pow(Y-y_model,2))
train_op = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

sess = tf.Session()
init_op = tf.global_variables_initializer()

sess.run(init_op)

# 训练
for epoch in range(training_epochs): 
    for (x, y) in zip(train_X, train_Y): 
        sess.run(train_op, feed_dict={X: x, Y: y})

w_val = sess.run(w)
print(w_val) 

sess.close()

plt.scatter(train_X, train_Y)

train_Y2 = 0
for i in range(num_coeffs):
    train_Y2 += w_val[i] * np.power(train_X, i)
plt.plot(train_X, train_Y2, 'r') 
plt.show() 