% 神经网络的均方误差

clear all;clc;

% 创建BP网络
net = newff([-10 10],[4 1],{'tansig','purelin'});

p = [-10 -5 0 5 10];
t = [0 0 1 1 1];
disp('网络仿真值:')
y = sim(net,p)
disp('绝对误差值:')
e = t - y
disp('均方误差性能')
perf = mse(e)