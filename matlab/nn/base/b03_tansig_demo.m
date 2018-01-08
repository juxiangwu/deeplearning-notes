% 双曲正切S型传递函数
clear all;clc;
n = -5 : 0.1 : 5;
a = tansig(n);
plot(n,a);grid on;
xlabel('输入数据');
ylabel('双曲正切S型传递函数')