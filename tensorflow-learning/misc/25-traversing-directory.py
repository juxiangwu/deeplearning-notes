#coding:utf-8
'''
Traversing Directory
'''

import tensorflow as tf
import os

curr_dir = os.getcwd()
filenames = tf.train.match_filenames_once(os.path.abspath(os.path.join(curr_dir,'/*.py')))
count_num_files = tf.size(filenames)
filename_queue = tf.train.string_input_producer(filenames)
reader = tf.WholeFileReader()
filename, file_contents = reader.read(filename_queue)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    num_files = sess.run(count_num_files)
    coord = tf.train.Coordinator() 
    threads = tf.train.start_queue_runners(coord=coord) 

for i in range(num_files):
    audio_file = sess.run(filename)
    print(audio_file) 