% 创建广义回归神经网络
% 广义回归神经网络适用于函数逼近

clear all;clc;

P = [1 2 3];
T = [2.0 4.1 5.9];

% 创建广义回归神经网络
net = newgrnn(P,T);
P = 1.5;
Y = sim(net,P)