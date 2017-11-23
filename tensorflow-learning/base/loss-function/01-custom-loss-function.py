import matplotlib.pyplot as plt
import tensorflow as tf

sess = tf.Session()
initialize_op = tf.global_variables_initializer()


x_vals = tf.linspace(-1.0 , 1 , 500)
target = tf.constant(0.0)

l2_y_vals = tf.square(target - x_vals)

sess.run(initialize_op)

l2_y_out = sess.run(l2_y_vals)
#print(l2_y_out)

l1_y_vals = tf.abs(target - x_vals)
l1_y_out = sess.run(l1_y_vals)

delta1 = tf.constant(0.25)
phuber1_y_vals = tf.multiply(tf.square(delta1),
                tf.sqrt(1.0 * tf.square((target - x_vals) / delta1)) - 1.0)

phuber1_out = sess.run(phuber1_y_vals)

delta2 = tf.constant(5.0)
phuber2_y_vals = tf.multiply(tf.square(delta2),
                tf.sqrt(1.0 * tf.square((target - x_vals) / delta2)) - 1.0)
phuber2_out = sess.run(phuber2_y_vals)

x_vals = tf.linspace(-3.,5.,500)
target = tf.constant(1.)
targets = tf.fill([500,],1.)

hinge_y_vals = tf.maximum(0.,1. - tf.multiply(target,x_vals))
hing_y_out = sess.run(hinge_y_vals)

xentropy_y_vals = tf.multiply(target,tf.log(x_vals)) - tf.multiply((1.0 - target),tf.log(1.0 - x_vals))
xentropy_y_out = sess.run(xentropy_y_vals)

xentropy_sigmoid_y_vals = tf.nn.sigmoid_cross_entropy_with_logits(labels = x_vals,logits = targets)
xentropy_sigmoid_y_out = sess.run(xentropy_sigmoid_y_vals)

weight = tf.constant(5.)
xentropy_weighted_y_vals = tf.nn.weighted_cross_entropy_with_logits(x_vals,targets , weight)
xentropy_weighted_y_out = sess.run(xentropy_weighted_y_vals)

unscaled_logits = tf.constant([[1.,-3.,10.]])
target_dist = tf.constant([[0.1,0.02,0.88]])
softmax_xentropy = tf.nn.softmax_cross_entropy_with_logits(labels = unscaled_logits,logits = target_dist)
print(sess.run(softmax_xentropy))

#unscaled_logits = tf.constant([[1.,-3.,10.]])
#sparse_target_dist = tf.constant([2.])
#sparse_xentropy = tf.nn.sparse_softmax_cross_entropy_with_logits(labels = unscaled_logits,logits = sparse_target_dist)
#print(sess.run(sparse_xentropy))

x_array = sess.run(x_vals)
plt.plot(x_array,l2_y_out,'b-',label = 'L2 Loss')
plt.plot(x_array,l1_y_out,'r--',label = 'L1 Loss')
plt.ylim(-0.2,0.4)
plt.legend(loc = "lower right",prop = {'size':1})
plt.show()