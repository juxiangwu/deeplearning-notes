#coding:utf-8
'''
卷积神经网络
'''
import mxnet as mx
from mxnet.gluon import nn 
from mxnet import ndarray as nd
from mxnet import gluon

try:
    ctx = mx.gpu()
    _ = nd.zeros((1,),ctx = ctx)
except:
    ctx = mx.cpu()

def transform(data,label):
    return data.astype('float32') / 255,label.astype('float32')

mnist_train = gluon.data.vision.FashionMNIST(train=True,transform=transform)
mnist_test = gluon.data.vision.FashionMNIST(train=False,transform=transform)

# 显示样本的形状和标号
data,label = mnist_train[0]
print('shape:',data.shape,',label:',label)

# def show_images(images):
#     n = images.shape[0]
#     _,figs = plt.subplots(1,n,figsize=(15,15))
#     for i in range(n):
#         figs[i].imshow(images[i].reshape((28,28)).asnumpy())
#         figs[i].axes.get_xaxis().set_visible(False)
#         figs[i].axes.get_yaxis().set_visible(False)

#     plt.show()

def get_text_labels(label):
    text_labels = [
        't-shirt','trouser','pullover','dress','coat',
        'sandal','shirt','sneaker','bag','ankle boot'
    ]

    return [text_labels[int(i)] for i in label]
# 显示数据
# data,label = mnist_train[0:9]
# show_images(data)
# print(get_text_labels(label))

# 读取数据
batch_size = 64
train_data = gluon.data.DataLoader(mnist_train,batch_size,shuffle=True)
test_data = gluon.data.DataLoader(mnist_test,batch_size,shuffle=False)

print('use contex:',ctx)

weight_scale = 0.01

# 输出通道 = 20,卷积核 kernel=(5,5)
W1 = nd.random_normal(shape=(20,1,5,5),scale=weight_scale,ctx=ctx)
b1 = nd.zeros(W1.shape[0],ctx=ctx)

# 输出通道=50,卷积核 kernel=(3,3)
W2 = nd.random_normal(shape=(50,20,3,3),scale=weight_scale,ctx=ctx)
b2 = nd.zeros(W2.shape[0],ctx=ctx)

# 输出维度=128
W3 = nd.random_normal(shape=(1250,128),scale=weight_scale,ctx=ctx)
b3 = nd.zeros(W3.shape[1],ctx=ctx)

# 输出维度=10
W4 = nd.random_normal(shape=(W3.shape[1],10),scale=weight_scale,ctx=ctx)
b4 = nd.zeros(W4.shape[1],ctx=ctx)

params = [W1,b1,W2,b2,W3,b3,W4,b4]

for param in params:
    param.attach_grad()

# 定义卷积神经网络模型
# 卷积层-激活层-池化层,然后转换成2D矩阵输出给后面的全连接层

def net(X,verbose=False):
    X = X.as_in_context(W1.context)

    # 第一层卷积
    h1_conv = nd.Convolution(data=X,weight=W1,bias=b1,
                kernel=W1.shape[2:],num_filter=W1.shape[0])
    # 第一层激活函数
    h1_activation = nd.relu(h1_conv)
    # 第一层池化层
    h1 = nd.Pooling(data=h1_activation,pool_type='max',kernel=(2,2),stride=(2,2))

    # 第二层卷积层
    h2_conv = nd.Convolution(data=h1,weight=W2,bias=b2,
                kernel=W2.shape[2:],num_filter=W2.shape[0])
    h2_activation = nd.relu(h2_conv)
    h2 = nd.Pooling(data=h2_activation,pool_type='max',kernel=(2,2))
    h2 = nd.flatten(h2)

    # 第一层全连接
    h3_linear = nd.dot(h2,W3) + b3
    h3 = nd.relu(h3_linear)

    # 第二层全连接
    h4_linear = nd.dot(h3,W4) + b4

    if verbose:
        print('1st conv block:', h1.shape)
        print('2nd conv block:', h2.shape)
        print('1st dense:', h3.shape)
        print('2nd dense:', h4_linear.shape)
        print('output:', h4_linear) 
    return h4_linear

# 定义精度计算
def accuracy(output,label):
    return nd.mean(output.argmax(axis=1) == label).asscalar()

# 估计模型精度
def evaluate_accuracy(data_iterator,net,ctx):
    acc = 0
    for data,label in data_iterator:
        label = label.as_in_context(ctx)
        output = net(data)
        acc += accuracy(output,label)
        return acc / len(data_iterator)

# 优化器
def SGD(params,lr):
    for param in params:
        param[:] = param - lr * param.grad

# 训练

softmax_cross_entropy = gluon.loss.SoftmaxCrossEntropyLoss()
learning_rate = .2
epochs = 5
for epoch in range(epochs):
    train_loss = 0.0
    train_acc = 0.0

    for data,label in train_data:
        # 复制到GPU
        label = label.as_in_context(ctx)
        with mx.autograd.record():
            output = net(data)
            loss = softmax_cross_entropy(output,label)
        loss.backward()
        SGD(params,learning_rate / batch_size)
        train_loss += nd.mean(loss).asscalar()
        train_acc += accuracy(output,label)

    test_acc = evaluate_accuracy(test_data, net, ctx)
    print("Epoch %d. Loss: %f, Train acc %f, Test acc %f" % (epoch, train_loss/len(train_data),
            train_acc/len(train_data), test_acc))

