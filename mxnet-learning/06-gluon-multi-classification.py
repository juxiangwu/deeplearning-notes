#coding:utf-8

from mxnet import ndarray as nd
from mxnet import autograd
from mxnet import gluon

def transform(data,label):
    return data.astype('float32') / 255,label.astype('float32')

# 定义精度计算
def accuracy(output,label):
    return nd.mean(output.argmax(axis=1) == label).asscalar()

# 估计模型精度
def evaluate_accuracy(data_iterator,net):
    acc = 0
    for data,label in data_iterator:
        output = net(data)
        acc += accuracy(output,label)
        return acc / len(data_iterator)

mnist_train = gluon.data.vision.FashionMNIST(train=True,transform=transform)
mnist_test = gluon.data.vision.FashionMNIST(train=False,transform=transform)

# 读取数据
batch_size = 256
train_data = gluon.data.DataLoader(mnist_train,batch_size,shuffle=True)
test_data = gluon.data.DataLoader(mnist_test,batch_size,shuffle=False)

# 定义和初始化模型
net = gluon.nn.Sequential()
with net.name_scope():
    net.add(gluon.nn.Flatten())
    net.add(gluon.nn.Dense(10))

net.initialize()

# 损失函数
softmax_cross_entropy = gluon.loss.SoftmaxCrossEntropyLoss()

# 优化器
trainer = gluon.Trainer(net.collect_params(),'sgd',{'learning_rate':0.1})

# 训练
epochs = 5
for epoch in range(epochs):
    train_loss = 0.0
    train_acc = 0.0

    for data,label in train_data:
        with autograd.record():
            output = net(data)
            loss = softmax_cross_entropy(output,label)
        loss.backward()
        trainer.step(batch_size)

        train_loss += nd.mean(loss).asscalar()
        train_acc += accuracy(output,label)
        print('epoch:%d,loss = %f,acc = %f'% (epoch,train_loss/ len(train_data),
                train_acc/ len(train_data)))
    test_acc = evaluate_accuracy(test_data,net)

    print('Epoch %d ,Loss: %f, Train_Acc:%f ,Test_Acc:%f.' %(epoch,
        train_loss / len(train_data),train_acc / len(train_data),test_acc ))

import matplotlib.pyplot as plt
def show_images(images):
    n = images.shape[0]
    _,figs = plt.subplots(1,n,figsize=(15,15))
    for i in range(n):
        figs[i].imshow(images[i].reshape((28,28)).asnumpy())
        figs[i].axes.get_xaxis().set_visible(False)
        figs[i].axes.get_yaxis().set_visible(False)
    plt.show()

def get_text_labels(label):
    text_labels = [
        't-shirt','trouser','pullover','dress','coat',
        'sandal','shirt','sneaker','bag','ankle boot'
    ]

    return [text_labels[int(i)] for i in label]

# 预测
data, label = mnist_test[0:9]
print('true labels')
print(get_text_labels(label))
predicted_labels = net(data).argmax(axis=1)
print('predicted labels')
print(get_text_labels(predicted_labels.asnumpy()))
# show_images(data)