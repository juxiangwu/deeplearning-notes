% 利用径向基神经网络实现函数逼近

clear all;clc;

x = -1 : 0.1 : 1;
T = cos(x * pi);
n = -3 : 0.1 : 3;
% 径向基神经元传递函数
a1 = radbas(n);
a2 = radbas(n - 1.2);
a3 = radbas(n + 2);

a = a1 + 1.2 * a2 + 0.6 * a3;
plot(n,a1,'+',n,a2,':',n,a3,n,a,'p');
xlabel('输入数据');
ylabel('加权曲线');
legend('径向基加权和 a1','径向基加权和 a2','径向基加权和 a3','径向基加权和 a')

net = newrb(x,T,0.025,1);
x1 = -1 : 0.01 : 1;
y = sim(net,x1)
figure;
plot(x1,y,x,T,'o')
legend('函数逼近曲线','原曲线')