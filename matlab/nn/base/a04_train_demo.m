% 实现一个或门输出
clear all;
clc;
P = [0 0 1 1;0 1 0 1];
T = [0 1 1 1];

% 构建一个感知器网络,权值为1
net = newp(minmax(P),1);
% 网络仿真,训练前的输出
disp('before train:')
Y = sim(net,P)
% 设置训练迭代次数
net.trainParam.epochs = 20;
net = train(net,P,T);
disp('after train:')
Y = sim(net,P)
% 计算神经网络的性能
err1 = mae(Y-T)
plotpv(P,T)
title('向量类别')
