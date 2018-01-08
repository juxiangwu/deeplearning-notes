% 创建概率神经网络。
% 概率神经网络是一种适用于分类问题的径向基神经网络

clear all;clc;

P = [1 2 3 4 5 6 7];
Tc = [1 2 3 2 2 3 1];
% 将数据索引转换为向量组
T = ind2vec(Tc)
% 创建概率神经网络
net = newpnn(P,T);
Y = sim(net,P)
% 将向量组转换为数据索引
Yc = vec2ind(Y)

