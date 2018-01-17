% 绘制神经网络和阈值在误差曲面图上的位置

clear all;clc;

X = [2.0 2.0];
T = [0.5 0.52];

W = -4 : 0.4 : 4;
b = W;

ES = errsurf(X,T,W,b,'logsig');
plotes(W,b,ES,[60 60]);

W = -2;b = 0;
net = newlind(X,T);
a = sim(net,X);
E = T - a;
e = sumsqr(E);
plotep(W,b,e)