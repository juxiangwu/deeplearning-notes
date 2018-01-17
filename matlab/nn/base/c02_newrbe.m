% 创建一个精确的径向基神经网络

clear all;clc;

P = [1 2 3];
T = [2.0 4.1 5.9];

net = newrbe(P,T);

P = 1.5;

Y = sim(net,P)