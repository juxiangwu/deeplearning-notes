% 使用newff创建BP网络

clear all;clc;

X = [1 2;-1 2;2 3];
T = [1 2;2 1];

net = newff(X,T,5);
net = train(net,X,T);

X1 = X;
disp('网络仿真结果:')
sim(net,X1)