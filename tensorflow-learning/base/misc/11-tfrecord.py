# -*- coding: utf-8 -*-
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import numpy as np

def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


MNIST_DIR = "E:/Develop/DeepLearning/datas/mnist"

mnist = input_data.read_data_sets(MNIST_DIR,dtype=tf.uint8,one_hot=True)

images = mnist.train.images
labels = mnist.train.labels

pixels = images.shape[1]
num_examples = mnist.train.num_examples

filename = "E:/Develop/DeepLearning/datas/mnist.tfrecord"
writer = tf.python_io.TFRecordWriter(filename)
print(num_examples)
for index in range(num_examples):
    image_raw = images[index].tostring()
    example = tf.train.Example(features=tf.train.Features(feature={
            "pixels":_int64_feature(pixels),
            "label":_int64_feature(np.argmax(labels[index])),
            "image_raw":_bytes_feature(image_raw)}
            ))
    print(index)
    writer.write(example.SerializeToString())

writer.close()
print("finished")