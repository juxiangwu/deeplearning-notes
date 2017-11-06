# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import tensorflow as tf

# 一定要使用 rb 模式
image_raw = tf.gfile.FastGFile("E:/t.jpg",'rb').read()

with tf.Session() as sess:
    image_data = tf.image.decode_jpeg(image_raw)
    #print(sess.run(image_data))
    plt.imshow(image_data.eval())
    plt.show()
    #image_data = tf.image.convert_image_dtype(image_data,dtype=tf.float32)
    encode_image = tf.image.encode_jpeg(image_data)
    with tf.gfile.GFile("output.jpg","wb") as f:
        f.write(encode_image.eval())