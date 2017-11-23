# -*- coding: utf-8 -*-

import tensorflow as tf
from skimage import io,transform
import numpy as np

#特征读取

#-----------------构建网络----------------------
#占位符
x=tf.placeholder(tf.float32,shape=[None,100,100,3],name='x')
y_=tf.placeholder(tf.int32,shape=[None,],name='y_')

#第一个卷积层（100——>50)
conv1=tf.layers.conv2d(
      inputs=x,
      filters=32,
      kernel_size=[5, 5],
      padding="same",
      activation=tf.nn.relu,
      kernel_initializer=tf.truncated_normal_initializer(stddev=0.01))
pool1=tf.layers.max_pooling2d(inputs=conv1, pool_size=[2, 2], strides=2)

#第二个卷积层(50->25)
conv2=tf.layers.conv2d(
      inputs=pool1,
      filters=64,
      kernel_size=[5, 5],
      padding="same",
      activation=tf.nn.relu,
      kernel_initializer=tf.truncated_normal_initializer(stddev=0.01))
pool2=tf.layers.max_pooling2d(inputs=conv2, pool_size=[2, 2], strides=2)

#第三个卷积层(25->12)
conv3=tf.layers.conv2d(
      inputs=pool2,
      filters=128,
      kernel_size=[3, 3],
      padding="same",
      activation=tf.nn.relu,
      kernel_initializer=tf.truncated_normal_initializer(stddev=0.01))
pool3=tf.layers.max_pooling2d(inputs=conv3, pool_size=[2, 2], strides=2)

#第四个卷积层(12->6)
conv4=tf.layers.conv2d(
      inputs=pool3,
      filters=128,
      kernel_size=[3, 3],
      padding="same",
      activation=tf.nn.relu,
      kernel_initializer=tf.truncated_normal_initializer(stddev=0.01))
pool4=tf.layers.max_pooling2d(inputs=conv4, pool_size=[2, 2], strides=2)

re1 = tf.reshape(pool4, [-1, 6 * 6 * 128])

#全连接层
dense1 = tf.layers.dense(inputs=re1, 
                      units=1024, 
                      activation=tf.nn.relu,
                      kernel_initializer=tf.truncated_normal_initializer(stddev=0.01),
                      kernel_regularizer=tf.nn.l2_loss)
dense2= tf.layers.dense(inputs=dense1, 
                      units=512, 
                      activation=tf.nn.relu,
                      kernel_initializer=tf.truncated_normal_initializer(stddev=0.01),
                      kernel_regularizer=tf.nn.l2_loss)
logits= tf.layers.dense(inputs=dense2, 
                        units=5, 
                        activation=None,
                        kernel_initializer=tf.truncated_normal_initializer(stddev=0.01),
                        kernel_regularizer=tf.nn.l2_loss)

#---------------------------网络结束---------------------------
#%%
#取出所有参与训练的参数
params=tf.trainable_variables()
print("Trainable variables:------------------------")

#循环列出参数
for idx, v in enumerate(params):
     print("  param {:3}: {:15}   {}".format(idx, str(v.get_shape()), v.name))

#%%
#读取图片
img=io.imread('d:/cat.jpg')
#resize成100*100
img=transform.resize(img,(100,100))
#三维变四维（100，100，3）-->(1,100,100,3)
img=img[np.newaxis,:,:,:]
img=np.asarray(img,np.float32)
sess=tf.Session()
sess.run(tf.global_variables_initializer()) 

#提取最后一个全连接层的参数 W和b
W=sess.run(params[26])
b=sess.run(params[27])

#提取第二个全连接层的输出值作为特征    
fea=sess.run(dense2,feed_dict={x:img})