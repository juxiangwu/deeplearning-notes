% 使用BFGS准牛顿BP算法训练神经网络

clear all;clc;
P = [0 1 2 3 4 5];
T = [0 0 0 1 1 1];
net = newff(P,T,2,{},'trainbfg');
a1 = sim(net,P)
net = train(net,P,T);
a2 = sim(net,P)