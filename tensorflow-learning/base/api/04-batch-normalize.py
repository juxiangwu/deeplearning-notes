# -*- coding:utf-8 -*-
'''
Batch Normalize
'''

import tensorflow as tf  
import numpy as np  
from tensorflow.python.ops import control_flow_ops  
from tensorflow.python.training import moving_averages  
  
def bn(x, is_training):  
    x_shape = x.get_shape()  
    params_shape = x_shape[-1:]  
  
    axis = list(range(len(x_shape) - 1))  
  
    beta = _get_variable('beta', params_shape, initializer=tf.zeros_initializer())  
    gamma = _get_variable('gamma', params_shape, initializer=tf.ones_initializer())  
  
    moving_mean = _get_variable('moving_mean', params_shape, initializer=tf.zeros_initializer(), trainable=False)  
    moving_variance = _get_variable('moving_variance', params_shape, initializer=tf.ones_initializer(), trainable=False)  
  
    # These ops will only be preformed when training.  
    mean, variance = tf.nn.moments(x, axis)  
    update_moving_mean = moving_averages.assign_moving_average(moving_mean, mean, BN_DECAY)  
    update_moving_variance = moving_averages.assign_moving_average(moving_variance, variance, BN_DECAY)  
    tf.add_to_collection(UPDATE_OPS_COLLECTION, update_moving_mean)  
    tf.add_to_collection(UPDATE_OPS_COLLECTION, update_moving_variance)  
  
    mean, variance = control_flow_ops.cond(  
        is_training, lambda: (mean, variance),  
        lambda: (moving_mean, moving_variance))  
  
    return tf.nn.batch_normalization(x, mean, variance, beta, gamma, BN_EPSILON)  