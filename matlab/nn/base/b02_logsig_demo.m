% logsig 函数

clear all;clc; 
n = -5 : 0.1 : 5;
a = logsig(n);
plot(n,a);grid on;
xlabel('输入数据');
ylabel('对数S型传递曲线');