% 线性神经网络自适应预测

clear all;clc;
T1 = 0 : 0.24 : 4;
T = sin(T1 * 5 * pi);
Q = length(T);

% 将信号T延时1~5个时间步长得到网络的输入
X = zeros(5,Q);
X(1,2:Q) = T(1,1:(Q-1));
X(2,3:Q) = T(1,1:(Q-2));
X(3,3:Q) = T(1,1:(Q-3));
X(4,3:Q) = T(1,1:(Q-4));
X(5,3:Q) = T(1,1:(Q-5));

figure;plot(T1,T);
hold on;
% 创建线性神经网络
net = newlind(X,T);
y = sim(net,X);
plot(T1,y,':',T1,'r',T-y,'r*');
xlabel('输入数据');
legend('网络待预测目标信号','网络预测输出','网络预测误差');
