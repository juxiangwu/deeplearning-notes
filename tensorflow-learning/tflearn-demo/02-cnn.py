# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import  
  
import tflearn  
from tflearn.layers.core import input_data, dropout, fully_connected  
from tflearn.layers.conv import conv_2d, max_pool_2d  
from tflearn.layers.normalization import local_response_normalization  
from tflearn.layers.estimator import regression  
#加载大名顶顶的mnist数据集（http://yann.lecun.com/exdb/mnist/）  
import tflearn.datasets.mnist as mnist  
X, Y, testX, testY = mnist.load_data('E:/Develop/DeepLearning/datas/mnist',one_hot=True)  
X = X.reshape([-1, 28, 28, 1])  
testX = testX.reshape([-1, 28, 28, 1])  
  
network = input_data(shape=[None, 28, 28, 1], name='input')  
# CNN中的卷积操作,下面会有详细解释  
network = conv_2d(network, 32, 3, activation='relu', regularizer="L2")  
# 最大池化操作  
network = max_pool_2d(network, 2)  
# 局部响应归一化操作  
network = local_response_normalization(network)  
network = conv_2d(network, 64, 3, activation='relu', regularizer="L2")  
network = max_pool_2d(network, 2)  
network = local_response_normalization(network)  
# 全连接操作  
network = fully_connected(network, 128, activation='tanh')  
# dropout操作  
network = dropout(network, 0.8)  
network = fully_connected(network, 256, activation='tanh')  
network = dropout(network, 0.8)  
network = fully_connected(network, 10, activation='softmax')  
# 回归操作  
network = regression(network, optimizer='adam', learning_rate=0.01,  
                     loss='categorical_crossentropy', name='target')  
  
# Training  
# DNN操作，构建深度神经网络  
model = tflearn.DNN(network, tensorboard_verbose=0)  
model.fit({'input': X}, {'target': Y}, n_epoch=20,  
           validation_set=({'input': testX}, {'target': testY}),  
           snapshot_step=100, show_metric=True, run_id='convnet_mnist')  
