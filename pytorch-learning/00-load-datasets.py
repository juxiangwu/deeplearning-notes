
#coding:utf-8
'''
加载数据
'''

from torchvision import transforms, datasets as ds
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np
#transform = transforms.Compose是把一系列图片操作组合起来，比如减去像素均值等。
#DataLoader读入的数据类型是PIL.Image
#这里对图片不做任何处理，仅仅是把PIL.Image转换为torch.FloatTensor，从而可以被pytorch计算
transform = transforms.Compose(
    [
        transforms.ToTensor()
    ]
)
data_dir = 'D:/Develop/DeepLearning/datasets/cifar10/cifar-10-batches-py'
train_set = ds.CIFAR100(root=data_dir, train=True, transform=transform, target_transform=None, 
                            download=False)

data_loader = DataLoader(dataset=train_set,
                         batch_size=1,
                         shuffle=False,
                         num_workers=2)

# # 生成torch.utils.data.DataLoaderIter
# # 不过DataLoaderIter它会被DataLoader自动创建并且调用，我们用不到
# data_iter = iter(data_loader)
# images, labels = next(data_iter)

