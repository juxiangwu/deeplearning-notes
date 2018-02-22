%% 绘制曲线
clear all;
clc;
% 定义输入向量和目标函数
P = [-0.5 -0.5 0.3 -0.1 -0.8;...,
     -0.5 0.5 -0.5 1.0 0.0];
T = [1 1 0 0 0];
 % 绘制样本点
 plotpv(P,T);
 
 % 构造神经网络
 net = newp([-40 1;-1 50],1);
 
 hold on
 % 返回分界线控点
 linehandle = plotpc(net.IW{1},net.b{1});
 net.adaptParam.passes = 3;
 linehandle = plotpc(net.IW{1},net.b{1});
 
 % 训练神经网络
 for a = 1 : 25
     [net,Y,E] = adapt(net,P,T);
     linehandle = plotpc(net.IW{1},net.b{1},linehandle);
     drawnow;
 end
 title('向量类别')
 