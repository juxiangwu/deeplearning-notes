# -*- coding: utf-8 -*-

import tensorflow as tf
import matplotlib.pyplot as plt


init = tf.global_variables_initializer()

img_path = ['E:\Images\20170728\20170727-C.jpg']
filename_queue = tf.train.string_input_producer(img_path)

reader = tf.WholeFileReader()
key, value = reader.read(filename_queue)

img_ts = tf.image.decode_jpeg(value, channels=3)

plt.figure('image')
with tf.Session() as sess:
    sess.run(init)
    #img = sess.run(img_ts)
    img = tf.to_float(img_ts) / 255.0;
    print(img)
    print(img_ts)
    img_dat = sess.run(img);
    #plt.subplot(111)
    #plt.imshow((img_ts / 255.0))
    #plt.imshow(img_ts.reshape(img_ts.shape[0], img_ts.shape[1]), cmap=plt.cm.Greys)
    plt.subplot(111)
    plt.imshow(img_dat)
    plt.show()
    