% 通过随机梯度方法计算网络权值与阈值的变化率

clear all;clc;
gW = rand(3,2);
lp.lr = 0.5;
dW = learngd([],[],[],[],[],[],[],gW,[],[],lp,[])
