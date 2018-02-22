% 对BP网络进行梯度下降学习

clear all;clc;
p = [-1 -1 2 2;0 5 0 5];
t = [-1 -1 1 1];
net = newff(p,t,3,{},'traingd');

% 设置网络参数
net.divideFcn = '';
net.trainParam.show = 50;
net.trainParam.lr = 0.05;
net.trainParam.epochs = 300;
net.trainParam.goal = 1e-5;

a = sim(net,p)
net = train(net,p,t);
a = sim(net,p)
