% 对线性神经网络进行自适应训练
clear all;
p1 = { -1 0 1 0 1 1 -1  0 -1 1 0 1};
t1 = { -1 -1 1 1 1 2 0 -1 -1 0  1 1};

% 构建线性神经网络
net = linearlayer([0 1],0.5);
[net,y,e,pf] = adapt(net,p1,t1);
%对神经网络进行自适应训练
while (mae(e) < 1e-20)
    [net,y,e,pf] = adapt(net,p1,t1);
end
% 输出平均绝对误差
mae(e)