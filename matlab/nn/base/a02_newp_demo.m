% 感知器网络

P = [0 2];
T = [0 1];

% 生成神经网络
net = newp([0 1;-2 2],1);
net.inputweights{1,1}.initFcn = 'rands';
net.biases{1}.initFcn = 'rands';
w = net.iw{1,1}
b = net.b{1}
