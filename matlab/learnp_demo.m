% 利用learnp函数对感知器网络进行训练,实现‘或’门
clear all;
clc;
% 期望误差最小值
err_goal = 0.0015;
% 最大训练次数
max_epoch = 9999;
% 样本数据
X = [0 1 0 1;0 1 1 0];
% 目标数据
T = [0 1 1 1];
% 创建感知器网络
net = newp([0 1;0 1],1);
W = rand(1,2);
b = rand;
net.iw{1,1} = W;
net.b{1} = b;

for epoch = 1:max_epoch
    y = sim(net,X);
    E = T - y;
    sse = mae(E);
    if( sse < err_goal)
        break;
    end
    % 训练
    dW = learnp(W,X,[],[],[],[],E,[],[],[],[],[]);
    db = learnp(b,ones(1,4),[],[],[],[],E,[],[],[],[],[]);
    % 更新网络的参数
    W = W + dW;
    b = b + db;
    net.iw{1,1} = W;
    net.b{1} = b;
end
epoch,W,y
