#coding:utf-8

'''
K-Means
'''

import tensorflow as tf
import numpy as np

def initial_cluster_centroids(X,k):
    return X[0:k,:]

def assign_cluster(X,centerois):
    expanded_vectors = tf.expand_dims(X, 0)
    expanded_centroids = tf.expand_dims(centroids, 1) 
    distances = tf.reduce_sum(tf.square(tf.subtract(expanded_vectors, 
                expanded_centroids)),2) 
    mins = tf.argmin(distances, 0) 
    return mins

def recompute_centroids(X, Y): #E 
    sums = tf.unsorted_segment_sum(X, Y, k)
    counts = tf.unsorted_segment_sum(tf.ones_like(X), Y, k)
    return sums / counts

k = 2
max_iterations = 100 
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    X = np.random.randn(100,100)
    centroids = initial_cluster_centroids(X, k)
    i, converged = 0, False
    while not converged and i < max_iterations: 
        i += 1
        Y = assign_cluster(X, centroids)
        centroids = sess.run(recompute_centroids(X, Y))
    print(centroids)
