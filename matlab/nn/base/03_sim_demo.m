% 神经网络仿真
clear all;
net = newp([-2 2;-2 2],1);
% 设置权值与阈值
net.IW{1,1} = [-1,1];
net.b{1} = [1];
% 对网络进行仿真
p1 = [1;1];
a1 = sim(net,p1)
p2 = [1;-1];
a2 = sim(net,p2)
p3 = {[1;1],[1;-1]}
a3 = sim(net,p3)