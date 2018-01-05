# -*- coding:utf-8 -*-

import numpy as np
import tensorflow as tf
import os
from tensorflow.examples.tutorials.mnist import input_data

temp_dir = 'temp/mnist/tensorflow/'

def _int64_feature(value):
    return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))

def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

def convert_to(data_set,name):
    images = data_set.images
    labels = data_set.labels
    num_examples = data_set.num_examples
    print(labels[0])
    if images.shape[0] != num_examples:
        raise ValueError('Image size %d dose not match label size %d' %(images.shape[0],num_examples))
    print(images.shape)
    rows = 28 #images.shape[0] # 28
    cols = 28 #images.shape[1] # 28
    depth = 1 #images.shape[2] # 1

    filename = os.path.join(temp_dir,name+'.tfrecords')
    print('write:',filename)
    writer = tf.python_io.TFRecordWriter(filename)

    for index in range(num_examples):
        image_raw = images[index].tostring()
        # 写入协议缓冲区
        feature = {
            'height':_int64_feature(rows),
            "width":_int64_feature(cols),
            "depth":_int64_feature(depth),
            "label":_int64_feature(int(labels[index])),
            "image_raw":_bytes_feature(image_raw)
        }
        example = tf.train.Example(features=tf.train.Features(feature=feature))
        writer.write(example.SerializeToString())
    writer.close()

def main():
    data_sets = input_data.read_data_sets('temp/mnist', one_hot=True)
    convert_to(data_sets.train,'mnist-train')
    convert_to(data_sets.validation,'mnist-validation')
    convert_to(data_sets.test,'mnist-test')

if __name__ == '__main__':
    main()
