# -*- coding: utf-8 -*-
import tensorflow as tf

import tensorflow as tf
from numpy.random import RandomState

def get_weight(shape,lambda):
    var = tf.Variable(tf.random_normal(shape),dtype=tf.float32)
    tf.add_to_collection('losses',tf.contrib.layers.l2_regularizer(lambda)(var))
    return var