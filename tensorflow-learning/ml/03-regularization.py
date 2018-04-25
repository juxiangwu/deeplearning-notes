#coding:utf-8
'''
正则化
'''

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# 按照比例分割测试和训练数据值
def split_dataset(x_dataset,y_dataset,ratio):
    x_arr = np.arange(x_dataset.size)
    y_arr = np.arange(y_dataset.size)
    np.random.shuffle(x_arr)
    np.random.shuffle(y_arr)

    x_num_train = int(ratio * x_dataset.size)
    y_num_train = int(ratio * y_dataset.size)

    x_train = x_dataset[x_arr[0:x_num_train]]
    y_train = y_dataset[y_arr[0:y_num_train]]
    x_test = x_dataset[x_arr[x_num_train:x_dataset.size]]
    y_test = y_dataset[y_arr[y_num_train:y_dataset.size]]

    return x_train,x_test,y_train,y_test

learning_rate = 0.001
training_epochs = 1000
reg_lambda = 0.0

x_dataset = np.linspace(-1,1,101)

# 多项式系数个数
num_coeffs = 9
y_dataset_params = [0.0] * num_coeffs
y_dataset_params[2] = 1
y_dataset = 0
for i in range(num_coeffs):
    y_dataset += y_dataset_params[i] * np.power(x_dataset,i)

y_dataset += np.random.randn(*x_dataset.shape) * 0.33

(x_train,x_test,y_train,y_test) = split_dataset(x_dataset,y_dataset,0.7)

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

def model(X,w):
    terms = []

    for i in range(num_coeffs):
        term = tf.multiply(w[i],tf.pow(X,i))
        terms.append(term)
    
    return tf.add_n(terms)

w = tf.Variable([0.] * num_coeffs,name='parameters',dtype=tf.float32)
y_model = model(X,w)

# 定义正则化损失函数
cost = tf.div(tf.add(tf.reduce_sum(tf.square(Y-y_model)),
        tf.multiply(reg_lambda, tf.reduce_sum(tf.square(w)))),
        2*x_train.size)

train_op = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

init_op = tf.global_variables_initializer()

sess = tf.Session()

sess.run(init_op)

for reg_lambda in np.linspace(0,1,100):
    for epoch in range(training_epochs):
        sess.run(train_op,feed_dict={X:x_train,Y:y_train})
    final_cost = sess.run(cost,feed_dict={X:x_test,Y:y_test})
    print('reg lambda:',reg_lambda)
    print('final cost:',final_cost)

sess.close()