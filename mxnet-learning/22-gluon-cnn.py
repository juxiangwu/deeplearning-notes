#coding:utf-8
'''
卷积神经网络
'''

from mxnet import gluon
from mxnet.gluon import nn
from mxnet import ndarray as nd
import mxnet as mx

def try_gpu():
    try:
        ctx = mx.gpu()
        _ = nd.zeros((1,),ctx=ctx)
    except:
        ctx = mx.cpu()
    return ctx


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


# 显示数据
# data,label = mnist_train[0:9]
# show_images(data)
# print(get_text_labels(label))

# 读取数据
batch_size = 64
train_data = gluon.data.DataLoader(mnist_train,batch_size,shuffle=True)
test_data = gluon.data.DataLoader(mnist_test,batch_size,shuffle=False)


# 定义网络模型
net = nn.Sequential()
with net.name_scope():
    net.add(nn.Conv2D(channels=20,kernel_size=5,activation='relu'),
    nn.MaxPool2D(pool_size=2,strides=2),
    nn.Conv2D(channels=50,kernel_size=3,activation='relu'),
    nn.MaxPool2D(pool_size=2,strides=2),
    nn.Flatten(),
    nn.Dense(128,activation='relu'),
    nn.Dense(10))

ctx = try_gpu()
net.initialize(ctx = ctx)

loss = gluon.loss.SoftmaxCrossEntropyLoss()
trainer = gluon.Trainer(net.collect_params(),'sgd', {'learning_rate': 0.5})

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
        trainer.step(batch_size)
        train_loss += nd.mean(loss).asscalar()
        train_acc += accuracy(output,label)

    test_acc = evaluate_accuracy(test_data, net, ctx)
    print("Epoch %d. Loss: %f, Train acc %f, Test acc %f" % (epoch, train_loss/len(train_data),
            train_acc/len(train_data), test_acc))
