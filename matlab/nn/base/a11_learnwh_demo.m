% learnwh函数
% learnwh为Widrow-Hoff学习函数，也称delta准则或最小方差准则学习函数
% 它可以修改神经元的权值和阈值，使输出误差的平方和最小。

clear all;clc;
p = rand(2,1);
e = rand(3,1);
lp.lr = 0.5;
dW = learnwh([],p,[],[],[],[],e,[],[],[],lp,[])