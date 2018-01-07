# 加载TF 并加载数据
import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data

#设置输入参数
batch_size = 128
test_size = 256


# 初始化权值与定义网络结构，建构一个3个卷积层和3个池化层，一个全连接层和一个输出层的卷积神经网络
# 首先定义初始化权重函数
def init_weights(shape):
    return tf.Variable(tf.random_normal(shape, stddev=0.01))


# 第一组卷积层以及池化层，最后　droupout是为了防止过拟合，在模型训练的时候丢掉一些神经元
# padding表示对边界的处理，SAME表示卷积的输入和输出保持同样尺寸
def model(X, w, w2, w3, w4, w_o, p_keep_conv, p_keep_hidden):
    l1a = tf.nn.relu(tf.nn.conv2d(X, w,
                                  strides=[1, 1, 1, 1], padding='SAME'))
    l1 = tf.nn.max_pool(l1a, ksize=[1, 2, 2, 1],  # l1 shape=(?, 14, 14, 32)
                        strides=[1, 2, 2, 1], padding='SAME')
    l1 = tf.nn.dropout(l1, p_keep_conv)

    # 第二组卷积层及池化层，最后dropout一些神经元
    l2a = tf.nn.relu(tf.nn.conv2d(l1, w2,  # l2a shape=(?, 14, 14, 64)
                                  strides=[1, 1, 1, 1], padding='SAME'))
    l2 = tf.nn.max_pool(l2a, ksize=[1, 2, 2, 1],  # l2 shape=(?, 7, 7, 64)
                        strides=[1, 2, 2, 1], padding='SAME')
    l2 = tf.nn.dropout(l2, p_keep_conv)

    # 第三组卷积神经网络及池化层，同样，最后dropout一些神经元
    l3a = tf.nn.relu(tf.nn.conv2d(l2, w3,  # l3a shape=(?, 7, 7, 128)
                                  strides=[1, 1, 1, 1], padding='SAME'))
    l3 = tf.nn.max_pool(l3a, ksize=[1, 2, 2, 1],  # l3 shape=(?, 4, 4, 128)
                        strides=[1, 2, 2, 1], padding='SAME')
    l3 = tf.reshape(l3, [-1, w4.get_shape().as_list()[0]])  # reshape to (?, 2048)
    l3 = tf.nn.dropout(l3, p_keep_conv)
    # 全连接层
    l4 = tf.nn.relu(tf.matmul(l3, w4))
    l4 = tf.nn.dropout(l4, p_keep_hidden)
    # 输出层
    pyx = tf.matmul(l4, w_o)
    return pyx


# 导入数据
mnist = input_data.read_data_sets("temp/mnist/", one_hot=True)
# 定义四个变量，分别为输入训练图像矩阵及其标签，输入测试图像矩阵及其标签
trX, trY, teX, teY = mnist.train.images, mnist.train.labels, mnist.test.images, mnist.test.labels
# -1表示布考虑输入图片的数量，28*28为图片的像素数，1是通道(channel)的数量，
# 因MNIST图片为黑白，彩色图片通道是3
trX = trX.reshape(-1, 28, 28, 1)  # 28x28x1
teX = teX.reshape(-1, 28, 28, 1)  # 28x28x1

X = tf.placeholder("float", [None, 28, 28, 1])
Y = tf.placeholder("float", [None, 10])  # 10为识别图片的类别从0到9，共10个取值

# 定义模型函数
# 神经网络模型的构建函数，传入以下参数
# X：输入数据
# w: 每一层权重
w = init_weights([3, 3, 1, 32])  # 大小为3*3，输入的维度为1 ，输出维度为32
w2 = init_weights([3, 3, 32, 64])  # 大小为3*3,输入维度为32，输出维度为64
w3 = init_weights([3, 3, 64, 128])  # 大小为3*3,输入维度为64，输出维度为128
w4 = init_weights([128 * 4 * 4, 625])  # 全连接层，输入维度为128*4*4,也就是上一层的输出，输出维度为625
w_o = init_weights([625, 10])  # 输出层，输入的维度为625， 输出110维，代表10类（labels）

# p_keep_conv,p_keep_hidden:dropout 保留神经元比例
# 定义dropout的占位符keep_conv，表示一层中有多少比例的神经元被保留，生成网络模型，得到预测数据
# 在训练的时候把设定比例的节点改为0，避免过拟合
p_keep_conv = tf.placeholder("float")
p_keep_hidden = tf.placeholder("float")
py_x = model(X, w, w2, w3, w4, w_o, p_keep_conv, p_keep_hidden)

# 定义损失函数，采用tf.nn.softmax_cross_entropy_with_logists，作为比较预测值和真实值的差距
# 定义训练操作(train_op) 采用RMSProp算法作为优化器,
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=py_x, labels=Y))
train_op = tf.train.RMSPropOptimizer(0.001, 0.9).minimize(cost)
predict_op = tf.argmax(py_x, 1)


#训练模型和评估模型

#在会话中定义图，开始训练和评估
# Launch the graph in a session
with tf.Session() as sess:
    # you need to initialize all variabels
    tf.global_variables_initializer().run()

    for i in range(100):
        training_batch=zip(range(0,len(trX),batch_size),
                       range(batch_size,len(trX)+1,batch_size))
        for start, end in training_batch:
            sess.run(train_op, feed_dict={X: trX[start:end], Y: trY[start:end],
                                         p_keep_conv: 0.8, p_keep_hidden: 0.5})
                                       
    test_indices = np.arange(len(teX)) # Get A Test Batch
    np.random.shuffle(test_indices)
    test_indices = test_indices[0:test_size]

    print(i, np.mean(np.argmax(teY[test_indices], axis=1) ==
                    sess.run(predict_op, feed_dict={X: teX[test_indices],
                                                   p_keep_conv: 1.0,
                                                   p_keep_hidden: 1.0})))
                              #预测的时候设置为1 即对全部样本进行迭代训练